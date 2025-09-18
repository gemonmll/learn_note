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
> fairscale 优化和加速深度学习模型的训练过程
> ![Alt text](image-118.png)
> ![Alt text](image-119.png)
> **Tokenizer文件解读**
> tokenizer类用于将文本进行表计划和编解码
> chatformat类使用tokenizr类编码不同角色和内容的消息
> ![Alt text](image-120.png)
> 正确使用分词器非常重要
> ![Alt text](image-121.png)
> ![Alt text](image-122.png)
> 代码提供了一个强大的分词器和聊天格式化工具，将文本转为token序列，并将聊天对话格式转为模型能理解的
> ![Alt text](image-123.png)
> 分词器的作用，
> 文本分词(BPE）、token到id的映射(词汇表)、特殊标记的处理（加入bos,eos）、编码解码、处理大型文本
> ![Alt text](image-124.png)
> llama3中使用的特殊标记
> start_header_id、end_header_id、begin_of_text
> 引入特性标记和提示格式为与模型进行结构化交互提供了强大的机制
> ![Alt text](image-126.png)
> ![Alt text](image-125.png)
> special_tokens（meta定义）和tiktoken分词器（google开发）的词汇表之前有如下关系
> 主要应用在chat模式中，text补全模型并没有明确使用这些特殊标记
> ![Alt text](image-127.png)
> ![Alt text](image-128.png)
> ![Alt text](image-129.png)
> 特殊标记的添加方法
> system prompt\user\assistant
> ![Alt text](image-130.png)
> Message和Dialog的关系：
> Dialog是有多个Message组成的完整对话序列
> ![Alt text](image-131.png)
> 举例说明分词器处理流程
> 添加bos标记，添加userid
> ![Alt text](image-132.png)
> ![Alt text](image-133.png)
> ![Alt text](image-134.png)
> ![Alt text](image-135.png)
> **RMSNorm文件**
> 对每个时间步的隐藏状态向量进行归一化
> 每个时间步的输入向量被独立归一化，适用于处理变长序列和保持时间步间的独立性
> ![Alt text](image-136.png)
> ![Alt text](image-137.png)
> ![Alt text](image-138.png)
> 计算公式如下：
> ![Alt text](image-139.png)
> ![Alt text](image-140.png)
> ![Alt text](image-141.png)
> **swiglu激活函数**
> ![Alt text](image-142.png)
> **GQA实现**
> ![Alt text](image-143.png)
> **RoPE实现**
> ![Alt text](image-144.png)
> **KVCache实现**
> 初始化-》更新-》追加
> ![Alt text](image-145.png)
> ![Alt text](image-146.png)
> 代码中实现KVCache的方式
> ![Alt text](image-147.png)