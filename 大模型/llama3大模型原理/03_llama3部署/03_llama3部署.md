## **llama3部署**
> **阿里云实例创建**
> ![Alt text](image.png)
> **ollama介绍**
> ollama支持的model
> ![Alt text](image-1.png)
> **ollama部署llama3**
> ollama主要特点，包括本地化部署，模型管理，open-webUi集成，命令行交互，优化与微调
> 允许用户会模型进行优化，包括微调和强化学习
> ![Alt text](image-2.png)
> 部署步骤
> ![Alt text](image-3.png)
> ![Alt text](image-4.png)
> ![Alt text](image-5.png)
> **ollama3推理**
> 使用rest api 交互
> ollama有一个rest api 用于交互模型
> ![Alt text](image-6.png)
> ![Alt text](image-7.png)
> chat with a model
> ![Alt text](image-8.png)
> ![Alt text](image-9.png)
> ![Alt text](image-10.png)
> ![Alt text](image-11.png)
> **vllm部署llama3-8b-instruct**
> vllm是一个用于大模型推理和服务的库
> ![Alt text](image-12.png)
> 下载llama3模型文件
> ![Alt text](image-13.png)
> 安装vllm
> ![Alt text](image-14.png)
> 模型推理 两个模式
> ![Alt text](image-15.png)
> ![Alt text](image-16.png)
> **llama-factory 微调llama3模型**
> llama-factory 一种用于大型语言微调的工具
> ![Alt text](image-17.png)
> ![Alt text](image-18.png)
> ![Alt text](image-19.png)
> 相比chatglm官方的p-tuning微调项目，提供了3.7倍加速比
> ![Alt text](image-20.png)
> 支持的训练方法
> ![Alt text](image-21.png)