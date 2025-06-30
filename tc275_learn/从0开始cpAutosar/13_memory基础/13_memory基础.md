### 13 memory基础
> **目录**
> ![alt text](image.png)
> ### 1 memory相关硬件知识介绍
>  共有15个segment 
> 所用的pflash就在segment 8,
>  每个pf就是一个bank
> ![alt text](image-1.png)
> bank相当于一个更小的segment
> 单个bank不支持边读边写
> ![alt text](image-2.png)
> sector 逻辑扇区 物理扇区
> 最小可擦除单元
> ![alt text](image-3.png)
> page,最小可写单元
> ![alt text](image-4.png)
> ![alt text](image-5.png)
> burst模式，更大容量的写
> ![alt text](image-6.png)
> ![alt text](image-7.png)
> **memory中相关硬件知识**
> ![alt text](image-8.png)
> ecc问题
> ![alt text](image-9.png)
> ecc机制 会自动生成safety ecc code
> ![alt text](image-10.png)
> ecc影响
> 对于ram重新写，对于flash 数据填充或禁用ecc
> ![alt text](image-11.png)
> ### 2 存储模块整体介绍
> 存储相关模块整体介绍
> nvm:nonvolatile memory manager,统一按照block编号，不关心底层数据类型
> ![alt text](image-12.png)
> 调用关系（同步调用）
> ![alt text](image-13.png)
> 异步调用，真正写会有fls_mainfunciton中写 
> ![alt text](image-14.png)
> ### 3 fls模块介绍
> api规范
> ![alt text](image-15.png)
> 有的芯片需要check
> ![alt text](image-16.png)
> **操作模式**：normal 和 fast
> ![alt text](image-17.png)
> **access load** job开始时候，把flash access的代码放在ram中，最后卸载
> ![alt text](image-18.png)
> ### 4 fee模块
> 尽可能使各处flash同时达到使用寿命  
> 最常用double-sector算法
> ![alt text](image-19.png)
> double sector算法
> 每个sector有两个类型，stage page(erased valid)和data blocked(blk)
> ![alt text](image-20.png)
> stage page(sector擦除、sector有效)
> ![alt text](image-21.png)
> data block
> ![alt text](image-23.png)
> **sector switch 过程**
> ![alt text](image-24.png)
> ![alt text](image-25.png)
> ![alt text](image-26.png)
> **准静态数据块**
> 准静态数据块单独有管理器处理，数据量大，较少更新
> ![alt text](image-27.png)
> ![alt text](image-28.png)
> 有了qs之后的flash分布情况
> ![alt text](image-29.png)
> **virtual page size**
> 避免误操作相邻芯片，设计一个虚拟地址
> 达到隔离的目的，应为物理地址的整数倍
> erase all enable选项
> ![alt text](image-30.png)
> **两个工程数据共享**
> 要保证两个工程之前的配置完全相同
> ![alt text](image-32.png)
> blank check功能
> ![alt text](image-33.png)
> ### 5 nvm模块
> **实操部分**
> **添加fls fee memif nvm**
> **配置mcal**
> ![alt text](image-34.png)
> ![alt text](image-35.png)
> **添加函数映射**
> ![alt text](image-36.png)
> **把对应的模块添加**
> ![alt text](image-37.png)
> **添加dem模块避免编译报错，添加nvmblock**
> ![alt text](image-38.png)
> ![alt text](image-39.png)
> ![alt text](image-40.png)
> ![alt text](image-41.png)
> ![alt text](image-42.png)
> **添加一个dem client**
> ![alt text](image-43.png)
> ![alt text](image-44.png)
> **配置初始化**
> ![alt text](image-45.png)
> ![alt text](image-46.png)
> **新建几个测试的block,注意readall配置**
> ![alt text](image-47.png)
> ![alt text](image-48.png)
> ![alt text](image-49.png)
> **nvm关联到swc ,打开service port**
> ![alt text](image-50.png)
> ![alt text](image-51.png)
> ![alt text](image-52.png)
> **swc层配置 打开enable api usage**
> ![alt text](image-53.png)
> ![alt text](image-54.png)
> ![alt text](image-55.png)
> **解决一些编译问题（ramblock没有找到）**
> ![alt text](image-56.png)
> ![alt text](image-57.png)
> ![alt text](image-58.png)
> ![alt text](image-59.png)
> **调试过程**
> 测试nvm读写
> ![alt text](image-60.png)、
> 出现问题 det error id 0x15
> ![alt text](image-61.png)
> ![alt text](image-62.png)
> 调试，观察fee_write是否有被调用
> ![alt text](image-63.png)
> fls read write未被调用
> ![alt text](image-64.png)
> 查看fee_mainfunction是否调用
> ![alt text](image-65.png)
> ![alt text](image-66.png)
> 排查后发现，fls完成后需要notify,非常关键的配置(fls和fee模块都要配置)
> ![alt text](image-67.png)
> ![alt text](image-68.png)
> ![alt text](image-69.png)
> 重新再擦除下dflash后
> ![alt text](image-70.png)
> 测试结果正常
> ![alt text](image-71.png)