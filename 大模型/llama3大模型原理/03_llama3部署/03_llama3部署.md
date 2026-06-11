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
> **llama-factory 微调实战**
> 配置过程
> ![Alt text](image-22.png)
> lora微调
> 修改sft文件
> ![Alt text](image-23.png)
> ![Alt text](image-24.png)
> ![Alt text](image-25.png)
> ![Alt text](image-26.png)
> ![Alt text](image-27.png)
> 修改数据集文件
> ![Alt text](image-28.png)
> ![Alt text](image-29.png)
> ![Alt text](image-30.png)
> **大模型推理**
> 执行推理过程
> ![Alt text](image-31.png)
> ![Alt text](image-32.png)
> **大模型评估**
> MMLU 大规模的多任务语言理解基准测试
> ![Alt text](image-33.png)
> 修改eval yaml
> ![Alt text](image-34.png)
> ![Alt text](image-35.png)
> CEVLA任务
> ![Alt text](image-36.png)
> **lora 合并**
> 把sft文件和模型权重文件合并成为一个文件
> ![Alt text](image-37.png)
> 合并后的推理，就不需要加载sft模型了
> ![Alt text](image-38.png)
>
> **llama3医疗问答大模型实战**
> 数据集准备
> ![Alt text](image-39.png)
> ![Alt text](image-40.png)
> 训练 
> ![Alt text](image-41.png)
> ![Alt text](image-42.png)
> 大模型推理
> ![Alt text](image-43.png)
> ![Alt text](image-44.png)
> **qlora微调**
> qlora微调
> ![Alt text](image-45.png)
> ![Alt text](image-46.png)
> ![Alt text](image-47.png)
> ![Alt text](image-48.png)
> ![Alt text](image-49.png)