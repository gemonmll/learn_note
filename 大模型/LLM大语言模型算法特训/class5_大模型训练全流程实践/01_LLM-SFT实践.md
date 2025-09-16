## **SFT实践**
> sft一般说的是instuction tuning
> ft说的是广义上的微调
> ![Alt text](image.png)
> **prompt learning和instruction learning**
> 提示学习和指令学习
> ![Alt text](image-1.png)
> 例子 instruct 让模型有理解能力
> ![Alt text](image-2.png)
> **代码讲解**
> ![Alt text](image-3.png)
> sft流程
> 加载数据-》tokenize
> 基本原则
> 样本质量高
> 不需要很多（2000 5000）
> sft的时候不要算prompt的loss
> ![Alt text](image-4.png)
> ![Alt text](image-5.png)
> ![Alt text](image-6.png)
> **第二部分实际操作理论**
> **目录**
> ![Alt text](image-7.png)
> **2.1 gradio/streamlit**
> gradio官方例子
> ![Alt text](image-8.png)
> ![Alt text](image-9.png)
> temperature 概率生成超参数
> 按照概率采样
> ![Alt text](image-10.png)
> 简单演示参数说明
> 主要是调整调整temperature
> ![Alt text](image-11.png)
> ![Alt text](image-12.png)
> **2.2 本体推理**
> ![Alt text](image-16.png)
> GGML(GGUF)
> 本地量化
> ![Alt text](image-13.png)
> ![Alt text](image-14.png)
> GPTQ量化方法 针对GPU优化
> ![Alt text](image-15.png)
> ![Alt text](image-17.png)
> **2.3 服务端推理**
> tritonServer
> 张量并行
> ![Alt text](image-18.png)
> 使用示例
> ![Alt text](image-19.png)
> ![Alt text](image-20.png)
> SSE
> ![Alt text](image-21.png)
> **2.4 推理框架**
> ![Alt text](image-22.png)
> ![Alt text](image-23.png)
> ![Alt text](image-24.png)