## **Llama 3 代码解析**
> github site
> ![Alt text](image-76.png)
> 各文件功能简要描述
> ![Alt text](image-77.png)
> **completion chat text代码实战**
> chat 是微调模型
> ![Alt text](image-78.png)
> text completion 是预训练
> llama.build传入大模型构建参数
> ![Alt text](image-79.png)
> ![Alt text](image-80.png)
> ![Alt text](image-81.png)
> 补全模式，promt输入
> ![Alt text](image-82.png)
> ![Alt text](image-83.png)
> chat模式 列表输入（包括多轮对话的输入）
> ![Alt text](image-84.png)
> ![Alt text](image-85.png)
> ![Alt text](image-86.png)
> ![Alt text](image-87.png)
> few-shot 和 one-shot promt,提示中提供示例
> few-shot 提供了多个示例，提供了更好的上下文
> ![Alt text](image-88.png)
> 额外工具，fire是一个由google开发的python库，旨在将python函数快速转换为命令行接口（CLI）
> 适合快速创建和部署可以从终端运行的脚本
> ![Alt text](image-89.png)
> ![Alt text](image-90.png)
> **generation py文件解析**
> 使用pytorch和fairScale实现的llama3模型生成器
> 构建和加载模型检查点的方法，以及针对给定提示生成文本序列的功能，还定了处理文本完成和对话生成的方法，通过调用语言生成模型来生成文本。
> 模型加载、文本生成、对话生成
> ![Alt text](image-91.png)
> 代码主要组成部分
> ![Alt text](image-92.png)
> ![Alt text](image-93.png)
> ![Alt text](image-94.png)
> ![Alt text](image-95.png)
> generate方法和处理过程
> ![Alt text](image-96.png)
> ![Alt text](image-97.png)
> ![Alt text](image-98.png)
> ![Alt text](image-99.png)
> text补全模式和chat模式调用generate的方法
> 提高代码的重用性和模块化
> ![Alt text](image-100.png)
> 两种模式在生成prompt_tokens时有一些不同
> token编码方式也不相同
> 生成目标不同
> 生成结果后处理也不同
> ![Alt text](image-101.png)
> ![Alt text](image-102.png)
> ![Alt text](image-103.png)
> ![Alt text](image-104.png)
> 总结：completionPrediction和chat prediction区别
> ![Alt text](image-105.png)
> 下面给出两种编码后的tokens格式
> text模式
> ![Alt text](image-106.png)
> ![Alt text](image-107.png)
> ![Alt text](image-108.png)
> chat模式 添加特殊bos编码
> 角色非常重要，提供上下文信息，提供角色扮演
> 还需要经过tokenizer中定义的encode方法处理，添加特殊标记
> ![Alt text](image-109.png)
> ![Alt text](image-110.png)
> **model文件解析**
> 定义了transforemer模型
> 定义了完整的模型。包括词嵌入，位置编码、多头注意力机制
> ![Alt text](image-111.png)
> ![Alt text](image-112.png)
> ![Alt text](image-113.png)
> ![Alt text](image-114.png)
> model-args类
> ![Alt text](image-115.png)
> 类之间的关系
> ![Alt text](image-116.png)
> ![Alt text](image-117.png)