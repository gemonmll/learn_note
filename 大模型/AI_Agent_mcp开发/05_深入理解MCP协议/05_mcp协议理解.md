## **MCP介绍**
> **1 MCP介绍**
> 大模型和外部工具交互的标准化协议
> ![Alt text](image.png)
> **2 MCP原理**
> mcp原理 客户端-》协议中心-》服务端
> 核心原理是将各个服务封装成ai能理解的tools
> 两类服务（远程服务，本地服务）
> ![Alt text](image-1.png)
> ![Alt text](image-2.png)
> MCP的应用
> ![Alt text](image-3.png)
> 开源社区 mcp server
> ![Alt text](image-4.png)
> 基于mcp的智能体架构
> ![Alt text](image-5.png)
> **高德MCP服务接入**
> mcp服务
> ![Alt text](image-6.png)
> 接入 MCP Server
> sse 远程接入
> ![Alt text](image-7.png)
> ![Alt text](image-8.png)
> 代码实现
> 高德MCP服务集成
> ![Alt text](image-9.png)
> 开发mcp客户端
> ![Alt text](image-14.png)
> ![Alt text](image-13.png)
> 查看有哪些tools
> ![Alt text](image-15.png)
> **结合智能体具备位置提供能力**
> ![Alt text](image-16.png)
> 获取mcp工具
> ![Alt text](image-17.png)
> ![Alt text](image-18.png)
> 创建智能体
> ![Alt text](image-19.png)
> 提示词
> ![Alt text](image-20.png)
> 异步运行智能体
> ![Alt text](image-21.png)
> **高德mcp可视化展示**
> 提示词优化
> ![Alt text](image-22.png)
> 结合本地文件工具
> 增加文件工具
> ![Alt text](image-23.png)
> 扩展智能体工具
> ![Alt text](image-24.png)
> **MCP通讯协议之stdio——实现本地MCP服务端和客户端**
> 三种通信方式（stdio \sse \streamable http）
> stdio 本地进程间通讯
> ![Alt text](image-25.png)
> 基于stdio的服务搭建
> 四个步骤
> ![Alt text](image-26.png)
> 总体架构
> ![Alt text](image-27.png)