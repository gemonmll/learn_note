import torch
import torch.nn as nn
import math
import numpy as np
# [新增] 引入pad_sequence工具
from torch.nn.utils.rnn import pad_sequence


# -----------------------------------------------------------------------------
# 1. 位置编码 (Positional Encoding)
# -----------------------------------------------------------------------------
class PositionalEncoding(nn.Module):
    """
    位置编码层。
    由于Transformer模型本身不包含任何递归或卷积，它无法感知序列中词的位置信息。
    因此，我们需要将词在序列中的位置信息注入到模型中。
    该层通过将特定频率的正弦和余弦函数添加到输入嵌入中来实现这一点。
    """
    def __init__(self, embed_dim, max_len=5000):
        """
        初始化位置编码层。
        Args:
            embed_dim (int): 词嵌入的维度，也即位置编码的维度。
            max_len (int): 预先计算位置编码的最大序列长度。
        """
        super(PositionalEncoding, self).__init__()

        # 创建一个形状为 (max_len, embed_dim) 的零矩阵，用于存储位置编码
        pe = torch.zeros(max_len, embed_dim)

        # 创建一个形状为 (max_len, 1) 的张量，表示序列中的位置 (0, 1, ..., max_len-1)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)

        # 计算用于缩放位置的除法项。公式是 1 / (10000^(2i/d_model))
        # 在对数空间中计算可以提高数值稳定性
        div_term = torch.exp(torch.arange(0, embed_dim, 2).float() * (-math.log(10000.0) / embed_dim))

        # 使用正弦函数填充偶数索引的维度
        pe[:, 0::2] = torch.sin(position * div_term)
        # 使用余弦函数填充奇数索引的维度
        pe[:, 1::2] = torch.cos(position * div_term)

        # 增加一个批次维度 (batch_size=1)，使其能够与输入批次相加
        # pe shape: (1, max_len, embed_dim)
        pe = pe.unsqueeze(0)
        
        # 将位置编码矩阵注册为模型的缓冲区（buffer）。
        # 缓冲区是模型状态的一部分，但不是模型参数，因此不会在反向传播中更新。
        self.register_buffer('pe', pe)

    def forward(self, x):
        """
        前向传播。
        Args:
            x (torch.Tensor): 输入的嵌入张量，形状为 (batch_size, seq_len, embed_dim)。
        Returns:
            torch.Tensor: 添加了位置编码的输出张量，形状与输入相同。
        """
        # 将输入x与对应长度的位置编码相加。
        # self.pe[:, :x.size(1), :] 会切片出与输入序列等长的位置编码
        x = x + self.pe[:, :x.size(1), :]
        return x

# -----------------------------------------------------------------------------
# 2. 多头自注意力 (Multi-Head Attention)
# -----------------------------------------------------------------------------
class MultiHeadAttention(nn.Module):
    """
    多头注意力机制层。
    它允许模型在不同的表示子空间中共同关注来自不同位置的信息。
    这是通过将Q(查询)、K(键)、V(值)拆分为多个“头”来实现的。
    """
    def __init__(self, embed_dim, heads):
        """
        初始化多头注意力层。
        Args:
            embed_dim (int): 输入的嵌入维度。
            heads (int): 注意力头的数量。
        """
        super(MultiHeadAttention, self).__init__()
        self.embed_dim = embed_dim
        self.heads = heads
        self.head_dim = embed_dim // heads

        # 确保嵌入维度可以被头的数量整除
        assert self.head_dim * heads == embed_dim, "embed_dim a multiple of heads"

        # 定义用于生成 Q, K, V 的线性层
        self.fc_q = nn.Linear(embed_dim, embed_dim)
        self.fc_k = nn.Linear(embed_dim, embed_dim)
        self.fc_v = nn.Linear(embed_dim, embed_dim)
        
        # 定义最终的输出线性层
        self.fc_out = nn.Linear(embed_dim, embed_dim)

    def forward(self, query, key, value, mask=None):
        # 输入的 query, key, value 形状: (batch_size, seq_len, embed_dim)
        N = query.shape[0]  # 获取批次大小

        # 1. 线性变换并切分成多头
        # - .view() 将 embed_dim 维度拆分为 heads * head_dim
        # - .transpose(1, 2) 交换 heads 和 seq_len 维度，便于后续计算
        #   最终形状变为 (N, heads, seq_len, head_dim)
        q = self.fc_q(query).view(N, -1, self.heads, self.head_dim).transpose(1, 2)
        k = self.fc_k(key).view(N, -1, self.heads, self.head_dim).transpose(1, 2)
        v = self.fc_v(value).view(N, -1, self.heads, self.head_dim).transpose(1, 2)

        # 2. 计算缩放点积注意力分数
        # - (N, heads, query_len, head_dim) @ (N, heads, head_dim, key_len) -> (N, heads, query_len, key_len)
        energy = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.head_dim)

        # 3. 应用掩码 (Masking)
        # 如果提供了掩码，则将掩码中为0的位置的 energy 值填充为一个极小的负数，
        # 这样在 softmax 后，这些位置的权重将接近于0。
        if mask is not None:
            energy = energy.masked_fill(mask == 0, float("-1e20"))

        # 4. 计算注意力权重
        # 在最后一个维度（key_len维度）上进行 softmax，得到归一化的注意力权重
        attention = torch.softmax(energy, dim=-1)
        # attention 形状: (N, heads, query_len, key_len)

        # 5. 使用注意力权重对 V 进行加权求和
        # - (N, heads, query_len, key_len) @ (N, heads, value_len, head_dim) -> (N, heads, query_len, head_dim)
        #   (其中 key_len == value_len)
        out = torch.matmul(attention, v)

        # 6. 合并多头的结果
        # - .transpose(1, 2) 换回维度 -> (N, query_len, heads, head_dim)
        # - .contiguous() 保证内存连续性
        # - .view() 将最后两个维度合并回 embed_dim
        out = out.transpose(1, 2).contiguous().view(N, -1, self.embed_dim)
        
        # 7. 通过最终的线性层进行投影
        out = self.fc_out(out)
        return out

# -----------------------------------------------------------------------------
# 3. Transformer 基础模块 (用于 Encoder 和 Decoder)
# -----------------------------------------------------------------------------
class TransformerBlock(nn.Module):
    """
    Transformer 的基础构建模块。
    它由一个多头注意力子层和一个前馈神经网络子层组成。
    每个子层后面都跟着一个残差连接 (Add) 和层归一化 (Norm)。
    """
    def __init__(self, embed_dim, heads, forward_expansion=4):
        super(TransformerBlock, self).__init__()
        # 第一个子层：多头注意力
        self.attention = MultiHeadAttention(embed_dim, heads)
        self.norm1 = nn.LayerNorm(embed_dim)
        
        # 第二个子层：位置无关的前馈网络
        self.feed_forward = nn.Sequential(
            nn.Linear(embed_dim, forward_expansion * embed_dim),
            nn.ReLU(),
            nn.Linear(forward_expansion * embed_dim, embed_dim),
        )
        self.norm2 = nn.LayerNorm(embed_dim)

    def forward(self, value, key, query, mask):
        # 1. 通过多头注意力子层
        attention_out = self.attention(query, key, value, mask)
        
        # 2. 第一个残差连接和层归一化
        x = self.norm1(attention_out + query)
        
        # 3. 通过前馈网络子层
        forward_out = self.feed_forward(x)
        
        # 4. 第二个残差连接和层归一化
        out = self.norm2(forward_out + x)
        return out

# -----------------------------------------------------------------------------
# 4. 编码器 (Encoder)
# -----------------------------------------------------------------------------
class Encoder(nn.Module):
    """
    Transformer 的编码器部分，由 N 个 TransformerBlock 堆叠而成。
    负责处理输入序列，并生成一系列富含上下文信息的表示。
    """
    def __init__(self, vocab_size, embed_dim, num_layers, heads, pad_idx):
        super(Encoder, self).__init__()
        # 词嵌入层，将输入的词索引转换为密集向量
        self.embed = nn.Embedding(vocab_size, embed_dim, padding_idx=pad_idx)
        # 位置编码层
        self.pos_encoding = PositionalEncoding(embed_dim)
        
        # 堆叠 N 个 TransformerBlock
        self.layers = nn.ModuleList(
            [TransformerBlock(embed_dim, heads) for _ in range(num_layers)]
        )

    def forward(self, x, mask):
        # 1. 将输入索引通过嵌入层和位置编码层
        x = self.embed(x)
        x = self.pos_encoding(x)
        
        # 2. 依次通过 N 个 TransformerBlock
        for layer in self.layers:
            # 在Encoder的自注意力中, Query, Key, Value 都来自同一输入 x
            x = layer(x, x, x, mask)
            
        return x

# -----------------------------------------------------------------------------
# 5. 解码器模块 (DecoderBlock)
# -----------------------------------------------------------------------------
class DecoderBlock(nn.Module):
    """
    Transformer 解码器的基础构建模块。
    与 EncoderBlock 不同，它包含两个注意力子层：
    1. 遮蔽多头自注意力 (Masked Multi-Head Self-Attention)
    2. 交叉注意力 (Cross-Attention)，关注编码器的输出
    """
    def __init__(self, embed_dim, heads):
        super(DecoderBlock, self).__init__()
        # 第一个子层：遮蔽多头自注意力
        self.attention = MultiHeadAttention(embed_dim, heads)
        self.norm = nn.LayerNorm(embed_dim)
        
        # 第二个子层：交叉注意力（封装在TransformerBlock中）
        self.transformer_block = TransformerBlock(embed_dim, heads)
        
    def forward(self, x, value, key, src_mask, trg_mask):
        # 1. 遮蔽多头自注意力
        # Q, K, V 都来自解码器自身的输入 x，使用 trg_mask 来防止关注未来的词
        attention = self.attention(x, x, x, trg_mask)
        query = self.norm(attention + x) # 残差连接和层归一化
        
        # 2. 交叉注意力
        # Query 来自解码器（上一步的输出query），Key和Value 来自编码器的最终输出
        # 使用 src_mask 来忽略源序列中的填充部分
        out = self.transformer_block(value, key, query, src_mask)
        return out

# -----------------------------------------------------------------------------
# 6. 解码器 (Decoder)
# -----------------------------------------------------------------------------
class Decoder(nn.Module):
    """
    Transformer 的解码器部分，由 N 个 DecoderBlock 堆叠而成。
    负责根据编码器的输出和已经生成的部分目标序列，来预测下一个词。
    """
    def __init__(self, vocab_size, embed_dim, num_layers, heads, pad_idx):
        super(Decoder, self).__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim, padding_idx=pad_idx)
        self.pos_encoding = PositionalEncoding(embed_dim)
        self.layers = nn.ModuleList(
            [DecoderBlock(embed_dim, heads) for _ in range(num_layers)]
        )
        # 最终的线性层，将输出映射到目标词汇表大小
        self.fc_out = nn.Linear(embed_dim, vocab_size)

    def forward(self, x, enc_out, src_mask, trg_mask):
        # 1. 目标序列的嵌入和位置编码
        x = self.embed(x)
        x = self.pos_encoding(x)
        
        # 2. 依次通过 N 个 DecoderBlock
        for layer in self.layers:
            # 传入编码器的输出 (enc_out) 用于交叉注意力
            x = layer(x, enc_out, enc_out, src_mask, trg_mask)
        
        # 3. 通过最终的线性层得到 logits
        out = self.fc_out(x)
        return out

# -----------------------------------------------------------------------------
# 7. 完整的 Transformer 模型
# -----------------------------------------------------------------------------
class Transformer(nn.Module):
    """
    完整的 Transformer 模型，由一个 Encoder 和一个 Decoder 组成。
    """
    def __init__(self, src_vocab_size, trg_vocab_size, embed_dim, num_layers, heads, src_pad_idx, trg_pad_idx):
        super(Transformer, self).__init__()
        # 编码器
        self.encoder = Encoder(src_vocab_size, embed_dim, num_layers, heads, src_pad_idx)
        # 解码器
        self.decoder = Decoder(trg_vocab_size, embed_dim, num_layers, heads, trg_pad_idx)
        # 源序列和目标序列的填充符索引
        self.src_pad_idx = src_pad_idx
        self.trg_pad_idx = trg_pad_idx

    def make_src_mask(self, src):
        """
        创建源序列的掩码，用于在自注意力中忽略填充（padding）部分。
        """
        # src 形状: (N, src_len)
        # 掩码形状: (N, 1, 1, src_len)
        src_mask = (src != self.src_pad_idx).unsqueeze(1).unsqueeze(2)
        return src_mask.to(src.device)

    def make_trg_mask(self, trg):
        """
        创建目标序列的掩码，它是一个组合掩码：
        1. 忽略填充（padding）部分。
        2. 防止解码器在预测当前词时关注到未来的词（因果关系掩码）。
        """
        N, trg_len = trg.shape
        # 创建一个下三角矩阵来实现因果关系掩码
        # trg_mask 形状: (N, 1, trg_len, trg_len)
        trg_mask = torch.tril(torch.ones((trg_len, trg_len), device=trg.device)).expand(
            N, 1, trg_len, trg_len
        )
        return trg_mask

    def forward(self, src, trg):
        """
        模型的前向传播。
        """
        # 1. 创建源序列和目标序列的掩码
        src_mask = self.make_src_mask(src)
        trg_mask = self.make_trg_mask(trg)
        
        # 2. 将源序列输入编码器
        enc_src = self.encoder(src, src_mask)
        
        # 3. 将编码器输出和目标序列输入解码器
        out = self.decoder(trg, enc_src, src_mask, trg_mask)
        return out
# -----------------------------------------------------------------------------
# 训练和测试 (使用规律数据和批处理)
# -----------------------------------------------------------------------------

# 1. [修改] 设置超参数
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device = torch.device("cpu")
BATCH_SIZE = 10  # [新增] 定义批处理大小
PAD_IDX = 0      # [新增] 定义填充符的索引为0
SOS_IDX = 1      # [修改] 定义SOS索引为1 (Start of Sequence)
EOS_IDX = 2      # [修改] 定义EOS索引为2 (End of Sequence)

# [修改] 更新词汇表大小，因为加入了PAD, SOS, EOS，数字从3开始
# 0:PAD, 1:SOS, 2:EOS, 3-12:数字0-9
SRC_VOCAB_SIZE = 13
TRG_VOCAB_SIZE = 13
EMBED_DIM = 64
NUM_LAYERS = 2
HEADS = 4

# 2. 实例化模型
model = Transformer(
    src_vocab_size=SRC_VOCAB_SIZE,
    trg_vocab_size=TRG_VOCAB_SIZE,
    embed_dim=EMBED_DIM,
    num_layers=NUM_LAYERS,
    heads=HEADS,
    src_pad_idx=PAD_IDX,
    trg_pad_idx=PAD_IDX
).to(device)

# 3. 定义优化器和损失函数 (忽略PAD_IDX的损失)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss(ignore_index=PAD_IDX)


# 4. [修改] 生成单个序列的函数 (使用新词汇表)
def generate_patterned_sequence(step):
    pattern_type = step % 3
    length = np.random.randint(4, 9)
    
    # [修改] 数字范围现在是 3-12
    # if pattern_type == 0:
    #     start = np.random.randint(3, 13 - length)
    #     seq = np.arange(start, start + length)
    #     src_seq = seq[::-1]
    # elif pattern_type == 1:
    #     pool = np.arange(3, 13)
    #     np.random.shuffle(pool)
    #     src_seq = pool[:length]
    # else:
    #     seq = np.random.randint(3, 8, size=length)
    #     src_seq = seq.copy()

    start = np.random.randint(3, 13 - length)
    seq = np.arange(start, start + length)
    src_seq = seq[::-1]

    trg_seq = np.sort(src_seq)
    src = np.concatenate(([SOS_IDX], src_seq, [EOS_IDX]))
    trg = np.concatenate(([SOS_IDX], trg_seq, [EOS_IDX]))
    return torch.tensor(src).long(), torch.tensor(trg).long()

# 5. [新增] 批处理数据生成和填充函数
def generate_batch(batch_size, step):
    src_list, trg_list = [], []
    for i in range(batch_size):
        # 传入 step+i 确保每个样本的模式有变化
        src, trg = generate_patterned_sequence(step + i)
        src_list.append(src)
        trg_list.append(trg)

    # 使用pad_sequence进行填充
    src_batch = pad_sequence(src_list, batch_first=True, padding_value=PAD_IDX)
    trg_batch = pad_sequence(trg_list, batch_first=True, padding_value=PAD_IDX)
    return src_batch, trg_batch

# 6. [修改] 训练循环
print(f"开始使用 {NUM_LAYERS}-层 Transformer, BATCH_SIZE={BATCH_SIZE} 在 {device} 上进行训练...")
model.train()
for step in range(3001): # 可以适当减少训练步数
    optimizer.zero_grad()

    # [修改] 调用新的批处理生成器
    src, trg = generate_batch(BATCH_SIZE, step * BATCH_SIZE)
    src = src.to(device)
    trg = trg.to(device)

    # [修改] 无需 .unsqueeze(0)，数据已经是批处理好的
    trg_input = trg[:, :-1]
    trg_target = trg[:, 1:]

    output = model(src, trg_input)
    output = output.reshape(-1, TRG_VOCAB_SIZE)
    target = trg_target.reshape(-1)

    loss = criterion(output, target)
    loss.backward()
    optimizer.step()

    if step % 300 == 0:
        print(f"Step {step}, Loss: {loss.item():.4f}")

# 7. 推理/测试 (保持单样本测试，逻辑更清晰)
print("\n训练完成，开始测试...")
model.eval()
with torch.no_grad():
    for test_type in range(3):
        print(f"--- 测试模式 {test_type} ---")
        src_np, _ = generate_patterned_sequence(test_type)
        src = src_np.unsqueeze(0).to(device)

        trg_tokens = [SOS_IDX]
        max_len = len(src_np) + 2
        for _ in range(max_len):
            trg = torch.tensor(trg_tokens).unsqueeze(0).long().to(device)
            output = model(src, trg)
            pred_token = output.argmax(2)[:, -1].item()
            trg_tokens.append(pred_token)
            if pred_token == EOS_IDX:
                break
        
        # [修改] 映射回原始数字 (索引-3)
        input_seq = [str(x-3) for x in src_np.tolist() if x not in [SOS_IDX, EOS_IDX, PAD_IDX]]
        output_seq = [str(x-3) for x in trg_tokens if x not in [SOS_IDX, EOS_IDX, PAD_IDX]]

        print(f"输入: {' '.join(input_seq)}")
        print(f"预测输出: {' '.join(output_seq)}")