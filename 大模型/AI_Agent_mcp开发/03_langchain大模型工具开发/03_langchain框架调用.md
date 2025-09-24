> ## **langchain框架调用**
>目录 使用langchain调用通义千问
> ![Alt text](image.png)
> 绑定自定义工具
> ![Alt text](image-1.png)
> **实例化大模型**
> 大模型实例化
> ![Alt text](image-2.png)
> 使用secretstr对api进行加密
> ![Alt text](image-3.png)
> **大模型调用**
> 第一种方式，比较简单的场景
> ![Alt text](image-4.png)
> ![Alt text](image-5.png)
> 第二种方式 使用提示词模板功能
> ![Alt text](image-6.png)
> promptTemlate字符串提示模板，适用于文本补全任务
> ![Alt text](image-7.png)
> 使用示例
> ![Alt text](image-8.png)
> ![Alt text](image-9.png)
> 使用示例2 文本替换
> 创建提示词模板-》创建提示词
> ![Alt text](image-10.png)
> **chatprompttemplate 聊天提示器模板**
> 适用于聊天木星，输入是多轮对话的消息列表
> ![Alt text](image-11.png)
> 使用示例 
> 传入数组
> ![Alt text](image-12.png)
> ![Alt text](image-13.png)
> **chatmessageprompttemplate 消息模板**
> 抽象模板中的某一条消息
> 系统消息抽象 用户消息抽象
> ![Alt text](image-14.png)
> ![Alt text](image-15.png)
> 使用方法
> ![Alt text](image-16.png)
> **fewshotprompttemplate,少样本提示模板**
> 控制输出格式
> 用于少样本学习，包含示例，帮助模型推理任务
> ![Alt text](image-17.png)
> 使用示例
> ![Alt text](image-19.png)
> ![Alt text](image-18.png)
> 推理过程
> ![Alt text](image-21.png)
> **链式调用大模型**
> 重用模板类和使用场景
> ![Alt text](image-22.png)
> 链式调用
> ![Alt text](image-23.png)
> **自定义工具调用**
> 使用步骤
> ![Alt text](image-24.png)
> 第一二步 工具函数转为tool对象
> ![Alt text](image-25.png)
> 绑定对象
> ![Alt text](image-26.png)
> 调用大模型
> ![Alt text](image-27.png)
> 生成结果：
> tool_calls
> 只会生成一串message去自行进行调用
> ![Alt text](image-28.png)
> 最后一步：调用工具，通过智能体调用，而非大模型调用
> ![Alt text](image-29.png)
> ![Alt text](image-30.png)
> **tool装饰器注册工具+args_schema精确控制工具入参**
> 第二步转为tool对象，有两种方式
> ![Alt text](image-31.png)
> 第二种方式是通过装饰器，需要提供注释
> ![Alt text](image-34.png)
> ![Alt text](image-33.png)
> ![Alt text](image-36.png)
> 精确传入类型 args_schema
> ![Alt text](image-37.png)