## **langchain进阶实战 外挂知识库**
> rag中最重要的是一个retrieval模块 存储检索
> 检索后需要进行业务截断与重排
> ![Alt text](image-25.png)
> 代码讲解
> ![Alt text](image-26.png)
> 加载文件 chunk化（split,overlap）
> ![Alt text](image-27.png)
> 存到database (faiss) 序列化的内容
> 多使用 logger库 tyro loguru
> ![Alt text](image-28.png)
> 相关化搜索（similarity_search,bm25搜索）
> 多搜索融合ensembleRetriever
> ![Alt text](image-29.png)
> ![Alt text](image-30.png)
> ![Alt text](image-31.png)
> 构造promt (先定义一个template)
> ![Alt text](image-32.png)
> 定义一个chain (也是一个函数，函数就是一个DAG图)
> 解读chain 一系列runnable 序列
> search->template->prompt->model
> ![Alt text](image-33.png)
> ![Alt text](image-34.png)
> prompt会基于模板生成
> ![Alt text](image-35.png)
> 有无参考rag的比对
> ![Alt text](image-36.png)
> **## 第二部分 复杂化RAG**
> 复杂处理
> ![Alt text](image-37.png)
> ![Alt text](image-38.png)
> chain构建（标准问法）
> ![Alt text](image-39.png)
> ![Alt text](image-40.png)
> 重排documents
> 把检索的document也返回
> ![Alt text](image-41.png)
> chain两种输入，promt和dict
> ![Alt text](image-42.png)
> 部署过程fastapi
> ![Alt text](image-43.png)
> ![Alt text](image-44.png)
> ![Alt text](image-45.png)
> 面试时需要注意的问题
> ![Alt text](image-46.png)