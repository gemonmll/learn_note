## **LLaMa3详解**
> **LLaMa进化史**
> meta公司退出的开源大模型进化史
> llama3 上下文8192个token，词表128k
> ![Alt text](image.png)
> ![Alt text](image-1.png)
> ![Alt text](image-2.png)
> ![Alt text](image-3.png)
> ![Alt text](image-4.png)
> **llama3模型类型**
> 基础模型和指令微调模型
> ![Alt text](image-5.png)
> llama主要的几个变体
> ![Alt text](image-6.png)
> 指令微调变体和基础版模型几个区别
> 训练目标不同、训练数据不同、应用场景不同、交互方式不同、可控性不同、推理效率不同
> ![Alt text](image-7.png)
> **衍生模型**
> 基于LLAMA的微调，alpaca,vicuna,llava
> ![Alt text](image-8.png)
> ![Alt text](image-9.png)
> 一些术语的解释
> ![Alt text](image-10.png)
> alpaca模型（数据开源，性能接近chatgpt）
> ![Alt text](image-11.png)
> llava，一种新型的大型多模态模型，结合NLP和CV
> ![Alt text](image-12.png)
> **LLAMA3 模型架构和代码详解**
> 模型架构对比
> ![Alt text](image-13.png)
> llama3 模型架构
> 基于标准的transformer架构进行了多项改进，包括更高的效率
> ![Alt text](image-14.png)
> 分层堆叠，嵌入层，自注意力层、前馈网络层、前馈网络FFN、位置编码（RoPE）
> ![Alt text](image-15.png)
> 与传统架构的相同处
> 基础结构、前馈网络、多头自注意
> ![Alt text](image-16.png)
> 不同之处
> gqa、swiglu激活函数、rope位置编码
> ![Alt text](image-17.png)
> **RMSNorm归一化**
> 归一化技术，可以提高训练稳定性、加快收敛速度并改善模型泛化能力。
> ![Alt text](image-18.png)
> 两种常用归一化技术：层归一化
> 使得每个样本的激活值在特征维度上具有均值为0、方差为1的分布
> ![Alt text](image-19.png)
> ![Alt text](image-20.png)
> RMSNorm是一种简化版本的层归一化，不要计算均值和标准差
> ![Alt text](image-21.png)
> RMSNorm应用
> 提高训练效率、提高训练稳定性和泛化性能、预归一化的优势
> 相比传统架构，RMS放在自注意力和MLP之前
> 效率能提升10%
> ![Alt text](image-22.png)
> ![Alt text](image-23.png)
> ![Alt text](image-24.png)
> **SwiGLU激活函数**
> 影响模型性能的稳定性和泛化能力
> ![Alt text](image-25.png)
> 常见的激活函数 ReLU
> ![Alt text](image-26.png)
> GELU，基于高斯分布的激活函数
> ![Alt text](image-27.png)
> Swish，平滑且连续的激活函数，Transformer等模型应用广泛
> ![Alt text](image-28.png)
> ![Alt text](image-29.png)
> GLU(Gate linear Unit)
> 门控机制，动态选择机制，在模型中选择性传递信息
> 使用sigmoid输出一个介于0-1之间的权重矩阵，选择性让部分信息通过
> ![Alt text](image-30.png)
> ![Alt text](image-31.png)
> ![Alt text](image-32.png)
> SwiGLU激活函数
> 结合上面两种机制的激活函数
> ![Alt text](image-33.png)
> ![Alt text](image-34.png)
> ![Alt text](image-35.png)
> swiGLU的计算代价与性能优势
> 更好的泛化性能和稳定的梯度流
> 三次矩阵乘法
> ![Alt text](image-36.png)
> **RoPE位置编码**
> 位置编码是transfomer中确保模型能够理解序列顺序信息的重要部分
> RoPE作为一种新型的位置编码方法，平衡了绝对和相对位置编码的优点
> ![Alt text](image-37.png)
> 位置编码背景
> 绝对位置编码：为序列中的每个位置提供一个固定的嵌入
> 相对位置编码：为序列中每两个token的相对位置信息
> ![Alt text](image-38.png)
> 绝对位置编码
> ![Alt text](image-39.png)
> 相对位置编码，关注的是相对距离，而非绝对位置
> Aij= Qi * Kj + Qi * ri-j
> ![Alt text](image-40.png)
> RoPE的原理
> 结合了绝对和相对位置编码的优点
> 使用旋转矩阵对每个位置进行编码，并将相对位置信息引入自注意力操作中
> ![Alt text](image-41.png)
> 具体计算过程
> ![Alt text](image-42.png)
> ![Alt text](image-43.png)
> ![Alt text](image-44.png)
> 示意图（注意有d和m）,对于不同的m，旋转矩阵是不同的
> ![Alt text](image-45.png)
> ![Alt text](image-46.png)
> RoPE的相对位置编码特性
> q,k的点积，相对信息融入到自注意力机制
> 把m变成了j-i
> ![Alt text](image-47.png)
> ![Alt text](image-48.png)
> RoPE结合了相对位置编码和绝对位置编码的优点
> 具体示例
> ![Alt text](image-49.png)
> ![Alt text](image-50.png)
> RoPE的优点
> 引入相对位置信息，保持绝对位置信息，高效处理长序列
> ![Alt text](image-51.png)