## **Cursor+mcp接入**
> 魔塔mcp市场
> ![Alt text](image.png)
> Node环境搭建，js脚本的解释器
> nvm安装nodejs
> ![Alt text](image-1.png)
> ![Alt text](image-2.png)
> 全局安装 playwright-mcp-server
> ![Alt text](image-3.png)
> npx安装，不在本地全局安装，临时安装，使用后删除
> **1 langchain+mcp读取playright**
> 配置使用playwright服务器
> ![Alt text](image-4.png)
> 两种方式获取mcp工具
> ![Alt text](image-5.png)
> **2 langgraph+create_react_agent创建智能体**
> 使用官方推荐的库创建llm
> ![Alt text](image-6.png)
> ![Alt text](image-7.png)
> 结果如下
> ![Alt text](image-8.png)
> ![Alt text](image-9.png)
> ![Alt text](image-10.png)
> 输出的结构化处理
> ![Alt text](image-11.png)
> 结果如下
> ![Alt text](image-12.png)
> **3 cursor简介**
> cursor功能
> ![Alt text](image-13.png)
> mcp 功能
> ![Alt text](image-14.png)
> cursor+高德mcp
> 引入高德开发key
> ![Alt text](image-15.png)
> ![Alt text](image-16.png)
> ![Alt text](image-17.png)
> **4 cursor+github MCP工具集成**
> 步骤1 ： 集成Github MCP工具
> 使用mcp工具查询个人仓库
> ![Alt text](image-18.png)
> ![Alt text](image-19.png)
> ![Alt text](image-20.png)
> ![Alt text](image-21.png)
> 开发实现
> 实现vue-element快速迭代
> ![Alt text](image-22.png)
> **5 langgraph agent接入github MCP服务**
> 接入mcp client
> ![Alt text](image-24.png)
> 创建智能体
> ![Alt text](image-25.png)