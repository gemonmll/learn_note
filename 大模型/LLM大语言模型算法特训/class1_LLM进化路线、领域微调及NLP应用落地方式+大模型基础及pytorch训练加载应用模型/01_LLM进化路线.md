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
> ### 4 大模型差异
> 预训练数据规模
> ![Alt text](image-41.png)
> 训练架构差异
> （encoder-decoder）\(causal decoder)\(prefic decode)
> ![Alt text](image-42.png)
> ![Alt text](image-43.png)
> TOKENizer 差异
> bype-pair (BPE)、wordpiece、sentencepiece
> ![Alt text](image-44.png)
> 训练目标差异
> ![Alt text](image-45.png)
> 位置编码差异
> ![Alt text](image-46.png)
> 正则化位置差异
> ![Alt text](image-47.png)
> ![Alt text](image-48.png)
> 激活函数差异
> ![Alt text](image-49.png)
> 注意力机制差异
> ![Alt text](image-50.png)
> ![Alt text](image-51.png)
> ### 5 主流大模型-结构
> llama 结构
> ![Alt text](image-52.png)
> glm 结构
> ![Alt text](image-53.png)
> bloom 结构
> ![Alt text](image-54.png)
> 主流模型对比-tokenizer (llama token对于中文支持不好，容易乱码，而且非常慢)
> 想要修改的话需要改此表和微调
> ![Alt text](image-55.png)
> ![Alt text](image-56.png)
> 综合对比
> ![Alt text](image-57.png)
## 6 大模型评估
> 评估的对象 （基础模型 sft模型）
> ![Alt text](image-58.png)
> 基于GPT自动化评分 （打分、投票）
> ![Alt text](image-59.png)
> ![Alt text](image-60.png)
> 案例- LLMZoo自动化评测
> ![Alt text](image-61.png)
> ![Alt text](image-62.png)
> 基于特定任务评估-GLUE\CEVAL
> ![Alt text](image-63.png)
> ![Alt text](image-64.png)
> MT-Bench多轮评测
> ![Alt text](image-65.png)
> longBench长文本评测
> ![Alt text](image-66.png)
> CEVAL/CMMLU等知识评测
> ![Alt text](image-67.png)
> CMB-中文医疗领域评测
> ![Alt text](image-68.png)
> FinEval中文金融领域评测
> ![Alt text](image-69.png)
> 大模型评测汇总（https://github.com/MLGroupJLU/LLM-eval-survey）
> ![Alt text](image-70.png)
> ## **领域微调模型落地范式**
> 落地范式
> ![Alt text](image-71.png)
> ![Alt text](image-72.png)
> 具体例子
> 选择基座->买卡->数据->clean
> peet(lora)微调-》形成cama
> ![Alt text](image-73.png)
> 大模型推理，显存预估 （训练阶段，推理阶段）
> ![Alt text](image-74.png)
> 微调加速 - freeze
> ![Alt text](image-75.png)
> 微调加速 - LORA
> ![Alt text](image-76.png)
> 医学微调大模型
> ![Alt text](image-77.png)
> 大模型构造（多模态）
> ![Alt text](image-78.png)
> ![Alt text](image-79.png)
> ![Alt text](image-80.png)
> ## 7 赋能传统NLP
> 大模型应用前提认知
> 大模型封装成黑盒，之后做二次开发，
> ![Alt text](image-81.png)
> 大模型用于文档问答
> ![Alt text](image-82.png)
> ![Alt text](image-83.png)
> 表格问答
> ![Alt text](image-84.png)
> 问答范式
> ![Alt text](image-85.png)
> 文档智能范式
> ![Alt text](image-86.png)
> 大模型用于数据标注123
> ![Alt text](image-87.png)
> 知识图谱构建
> ![Alt text](image-88.png)
> ![Alt text](image-89.png)
> ![Alt text](image-90.png)
> ![Alt text](image-91.png)
> ![Alt text](image-92.png)
> ![Alt text](image-93.png)
> 数据库问答
> ![Alt text](image-94.png)