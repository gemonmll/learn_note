### 03 Memory解读
> 学习方法
> 学习关键（implementation specific 具体实施）
> 理解有些可以配置，有些必须要实现，有些是需要严格实现
> ![alt text](image.png)
> architecture 架构图 （ECU mcal）
> ![alt text](image-1.png)
> ![alt text](image-3.png)
> Memory 文档
> 第四章很重要
> ![alt text](image-4.png)
> ![alt text](image-6.png)
> ![alt text](image-7.png)
> 需求文档
> ![alt text](image-5.png)

### 3.2 EXP_NVDataHandling PDF解读、SRS解读
> 主要是三部分 （NVM特性、使用RTE、初始化RAM block）
> ![alt text](image-8.png)
> ![alt text](image-9.png)
>#### 基本存储结构（各种obj）
> ![alt text](image-10.png)
> ram block (可选)
> ![alt text](image-11.png)
> rom block (可选 不可修改)
> ![alt text](image-12.png)
> NV block(非易失 可修改)
> ![alt text](image-13.png)
> 管理块（临时 放在ram中，用来标记状态等，记录ERR, 必须要求的快）
> ![alt text](image-14.png)
>#### 块管理类型（更加高级）
> ![alt text](image-15.png)
> ![alt text](image-16.png)
> 冗余block 
> ![alt text](image-17.png)
> dataset 数组bLock
> ![alt text](image-18.png)
> #### 同步机制（显式同步， 隐式同步）
> 在swc与NVM之间的数据同步
> ![alt text](image-19.png)
> ![alt text](image-20.png)
> #### RTE访问
> ![alt text](image-21.png)
> 案例1
> ![alt text](image-22.png)
> #### SRS需求分析
> ![alt text](image-23.png)
> 功能需求（配置 初始化 常规 下电 错误处理）
> ![alt text](image-24.png)
> ![alt text](image-25.png)

### 3.3 各个sws解读
> 功能的描述 services ID
> ![alt text](image-26.png)
> 时序图
> NVM Init
> ![alt text](image-27.png)
> polling方式 BSWtask中调用
> ![alt text](image-28.png)
> callback
> ![alt text](image-29.png)
> cancellation
> ![alt text](image-30.png)

### 3.4 代码分析
> 代码架构（核心NVM 服务层）
> ![alt text](image-31.png)
> ![alt text](image-32.png)
> service ID 的对应
> ![alt text](image-33.png)
> ![alt text](image-34.png)
> 代码执行
> ![alt text](image-35.png)
> ![alt text](image-36.png)
> 真正的写入也会有一个线程
> ![alt text](image-37.png)
> 很多type是autosar规定的，必须实现
> ![alt text](image-38.png)
> ![alt text](image-40.png)
> ![alt text](image-39.png)