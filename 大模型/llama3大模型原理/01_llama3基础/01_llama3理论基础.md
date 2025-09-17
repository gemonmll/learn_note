## **理论基础**
> **目录**
> ![Alt text](image-1.png)
> ![Alt text](image.png)
> **注意力机制**
> ![Alt text](image-2.png)
> **Transformer原理**
> ![Alt text](image-3.png)
## **LLM的文本生成**
> LLM推理方式分为两种：预填充和续写
> ![Alt text](image-4.png)
> 通过这两种方式生成
> ![Alt text](image-5.png)
> 模型并无对话和上下文记忆功能，而是将之前所有的对话作为输入,生成新的token。
> 无真正的记忆
> 尽管大模型支持长度比较长，但还是要控制上下文长度
> ![Alt text](image-6.png)
> ![Alt text](image-7.png)
> ## **LLM的文本生成模式**
> 自回归模式生成，输出作为下一步的输入
> ![Alt text](image-8.png)
> LLM文本生成模式，completion模式和chat模式
> 文本补全和聊天
> ![Alt text](image-9.png)
> completion模式，最基础，给定提示自动补全
> ![Alt text](image-10.png)
> chat模式，模拟多轮对话，连贯互动
> ![Alt text](image-11.png)
> 小结
> chat模式还引入一些专门的技术 角色指令，rag
> ![Alt text](image-12.png)
> ## **LLM的文本生成策略**
> 文本生成的方法
> ![Alt text](image-13.png)
> greedy sampling
> 选择概率最高的token,但可能导致生成重复
> ![Alt text](image-14.png)
> beam search
> 考虑K个token
> 选择整体概率最高的分支
> ![Alt text](image-15.png)
> ![Alt text](image-16.png)
> Normal random sampling 正常随机抽样
> ![Alt text](image-17.png)
> random sampling with temperature
> 随机温度抽样
> 高温度适用于创意写作，低温度适用于事实回答
> ![Alt text](image-18.png)
> ![Alt text](image-19.png)
> ![Alt text](image-20.png)
> top-k sampling (top-k抽样)
> ![Alt text](image-21.png)
> top-p抽样
> 避免top-k引入不确定
> 选择累计概率
> ![Alt text](image-22.png)
> ![Alt text](image-23.png)
> ![Alt text](image-24.png)
> 生成策略比较与建议
> ![Alt text](image-25.png)
> ![Alt text](image-26.png)
> **token与分词器**
> 可能是单词 或是字符或是子词
> ![Alt text](image-27.png)
> 分词器 tokenizer->送入到embedding
> ![Alt text](image-28.png)
> 分词器常用分词方式
> 字典分词、BPE、SentiencePiece、WordPiece
> ![Alt text](image-29.png)
> 还有一些特殊token标识不同功能
> cls\sep\pad\unk\mask
> ![Alt text](image-30.png)
> llama3用的tiktoken分词器
> 平均每个单词会被分成1.3个token
> ![Alt text](image-31.png)
> 示例
> ![Alt text](image-32.png)
> llama2使用bpe和sentencepiece分词器
> 迭代地合并语料库中最频繁出现的字符
> ![Alt text](image-33.png)
> llama3分词器，更大的词汇量和TikToken
> ![Alt text](image-34.png)
> **LLM的文本生成过程**
> 主流LLM生成过程 decoder-only
> ![Alt text](image-35.png)
> 过程包括一下：
> 输入阶段-》分词-》嵌入-》位置编码-》transformer处理-》输出转换-》softmax-》采样-》生成文本-》后处理
> 位置编码：由于transformer模型不具备捕捉顺序的能力，通常会给每个嵌入向量添加一个位置编码
> ![Alt text](image-36.png)
> ![Alt text](image-37.png)
> ![Alt text](image-38.png)
> 举例
> ![Alt text](image-39.png)
> ![Alt text](image-40.png)
> ![Alt text](image-41.png)
> 解释
> ![Alt text](image-42.png)
> ![Alt text](image-43.png)
> ![Alt text](image-44.png)
> ![Alt text](image-45.png)
> ![Alt text](image-46.png)
> **prefill和decoder阶段**
> LLM生成文本过程中，通常会涉及两个阶段：预填充（prefill）和解码(decode)
> 首先需要一个开头
> ![Alt text](image-47.png)
> ![Alt text](image-48.png)
> prefill阶段：用于准备初始上下文，模型会处理输入的初始文本，并生成相应的内部状态（KV缓存）
> ![Alt text](image-49.png)
> 解码阶段：根据预填充阶段准备好的上下文，生成后续文本过程，逐步生成token，并在每次生成后更新kv缓存
> ![Alt text](image-50.png)
> 两个阶段的意义
> prefill提供出初始上下文，decode逐步生成文本
> ![Alt text](image-51.png)
> **LLAMA3 生成过程**
> 1) 经过分词器，产生一个seq_len(8k上下文窗口)的输入token序列，并且会将tokens映射到词汇表（128k）中对应的token IDs
> 2) 通过嵌入矩阵，映射成seq_len x 4096的嵌入表示矩阵，4096是llama指定的特征维度 
> 3) 经过transformer block层，32层堆叠
> 4) 最后转换回128k
> ![Alt text](image-53.png)
> ![Alt text](image-54.png)
> **文本生成时的qkv**
> query\key\value
> ![Alt text](image-55.png)