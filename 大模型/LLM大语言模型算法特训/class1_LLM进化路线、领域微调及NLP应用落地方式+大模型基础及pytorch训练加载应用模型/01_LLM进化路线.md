## 01 LLM 进化路线 领域微调 及NLP应用
> 目录
> ![Alt text](image.png)
> **模型训练基础目录**
> ![Alt text](image-1.png)
> **1.1 基本pipeline**
> ![Alt text](image-2.png)
> **1.2 训练模型基础**
> ![Alt text](image-3.png)
> ![Alt text](image-4.png)
> ![Alt text](image-5.png)
> ![Alt text](image-6.png)
> ## **2 cuda并行基础**
> **目录**
> ![Alt text](image-7.png)
> **2.1基本结构**
> ![Alt text](image-8.png)
> 性能指标 性能差距巨大
> ![Alt text](image-9.png)
> 内存模型
> ![Alt text](image-10.png)
> ![Alt text](image-11.png)
> **case study 矩阵乘法**
> ![Alt text](image-12.png)
> ![Alt text](image-13.png)
> ![Alt text](image-14.png)
> ## **3 LLM进化路线**
> **langchain 理论**
> ![Alt text](image-15.png)
> ![Alt text](image-16.png)
> **transformer系列演化**
> bert代表的encoder-only
> gpt代表的decoder-only
> ![Alt text](image-17.png)
> ![Alt text](image-18.png)
> ## **3.1大模型研发阶段**
> 预训练（时间最长）
> sft->rm->rlhf 微调->奖励->强化学习
> ![Alt text](image-19.png)
> **预训练模型分为两类 NLU和NLG**
> NLU bert 自然语言生成 (输出范围确定，评级方法明确)
> NLG 预训练模型 （输出自由度高，评价方法难，更具创造性）
> ![Alt text](image-20.png)
> **大模型的涌现能力（大力出奇迹）**
> ![Alt text](image-21.png)
> **gpt的模型演化之路**
> ![Alt text](image-22.png)
> **大模型本质-概率统计**
> 缩放法则（参数量越大，loss一定会降低）
> ![Alt text](image-23.png)
> 训练过程-无监督训练
> ![Alt text](image-24.png)
> 有监督微调 - SFT
> 通常采用混合预训练任务损失和下游微调损失
> ![Alt text](image-25.png)
> ![Alt text](image-26.png)
> 强化学习（PPO） 奖励学习（计算kl散度，调整loss函数）
> ![Alt text](image-27.png)
> ![Alt text](image-28.png)
> **大模型生成原理**
> ![Alt text](image-29.png)
> **top-k  top-p temperature策略**
> k值变大，选择范围变大，输出更加多样化但精度会降低
> ![Alt text](image-30.png)
> ![Alt text](image-31.png)
> ![Alt text](image-32.png)
> **大模型transformer**
> ![Alt text](image-33.png)
> 模型嵌入 绝对位置编码
> ![Alt text](image-34.png)
> 前馈层
> ![Alt text](image-35.png)
> 残差归一化
> ![Alt text](image-36.png)
> 编码解码
> ![Alt text](image-37.png)
> **预训练语言模型实践**
> 预训练词元分析器
> ![Alt text](image-38.png)
> ![Alt text](image-39.png)
> 模型训练，模型使用
> ![Alt text](image-40.png)