## langchain
> **langchain是什么**
> langchain\community\core
> ![Alt text](image.png)
> **大模型的优势**
> 处理用户输入prompt,简化prompt的形式
> 输入复杂、模型复杂、输出复杂
> 减少胶水代码
> ![Alt text](image-1.png)
> **langchain核心模块**
> chains将llm和其他模块相结合
> ![Alt text](image-2.png)
> **第一部分 langchain-models**
> models 三类模型（llm chat emebbing）
> ![Alt text](image-3.png)
> 没有langchain，openai的做法
> api不同
> ![Alt text](image-4.png)
> 三种使用方式（openai huggingface 本地）
> langchain 统一api接口 -llm模型
> 本地部署模型
> ![Alt text](image-5.png)
> chat和embedding模型使用
> ![Alt text](image-6.png)
> **第二部分 langChain-Promt**
> 一个好的promt是大模型获得良好效果的基础
> 思维链prompt 
> ![Alt text](image-8.png)
> prompt code 示例
> promptTemplate.from_template 用法2使用多
> ![Alt text](image-9.png)
> **第三部分 langchain-chain**
> 将LLM和其他模型组合、确定变量传递、统一接口
> ![Alt text](image-10.png)
> chain code example (prompt->chat)
> LCEL语法
> ![Alt text](image-11.png)
> 内部chain
> ![Alt text](image-12.png)
> **第四部分 langchain-retrieval 检索**
> 加载原始数据，vector store->query vector store
> ![Alt text](image-14.png)
> vector store 技术栈 faiss库 chroma库
> ![Alt text](image-13.png)
> vector store example
> ![Alt text](image-15.png)
> 检索方法 backed retriever,multiquery，contextual compression，long-context重新排序
> ![Alt text](image-16.png)
> ![Alt text](image-17.png)
> 本地知识库检索 example
> ![Alt text](image-18.png)
> **第五部分 langchain Memory**
> 记忆功能 （保留最近的K个对话）
> ![Alt text](image-19.png)
> code example
> memory本质是将conversation保存到history中
> ![Alt text](image-20.png)
> **第六部分 langchain Agents**
> agents和chain有区别，人工定义与llm决定
> 每一个agent都是一个LLM,可以执行特定功能的Agent是一个tool
> ![Alt text](image-21.png)
> example（function call）
> ![Alt text](image-22.png)
> ![Alt text](image-23.png)
> **建议**
> agent是锦上添花、用好chain可以实现大部分功能
> ![Alt text](image-24.png)