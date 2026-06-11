## 05 methodology 
### overview
> 传输标准文件
> ![alt text](image.png)

### current workflow(non-autosar) 
> 传统部件根据dbc fibex ldf 三个文件
> ![alt text](image-1.png)

### autosar workflow (标准流程)
> 分为四个文件（software component description\ system description\extract of system description\ ecu configuration description）
> ![alt text](image-2.png)

### 描述文件生成过程
> 从software component、系统输入、ecu资源描述为输入 生成系统配置文件
> ![alt text](image-3.png)

### swc swc描述文件
> 包括资源需求 接口适配 数据与操作
> ![alt text](image-4.png)

### ecu描述文件
> 传感器 执行器 外设
> ![alt text](image-5.png)

### system description
> 协议 波特率 等
> ![alt text](image-6.png)

### autosar oem与tier1 之间数据传输定义
> 通过ecuex文件进行接口描述
> ![alt text](image-7.png)
>
> ecuex 文件
> ecu性能描述 id 网络信号 pdu swc 端口配置
> ![alt text](image-8.png)
> ![alt text](image-9.png)
> 
>  t1和oem的几种分工模式
>  ![alt text](image-10.png)
>  ![alt text](image-11.png)
>  ![alt text](image-12.png)

### ecu configuration
> ecu 的配置
> ![alt text](image-13.png)
> ![alt text](image-14.png)

### 实现流程
> ![alt text](image-15.png)

### autosar 解决方案
> 一些额外的文件
> ![ ](image-16.png)
> vector 开发工具链
> vVIRTUALtarget 仿真
> ![alt text](image-17.png)
> preevision system design
> 软件架构设计
> ![alt text](image-18.png)
> ![alt text](image-19.png)
> vtt canoe 仿真测试
> ![alt text](image-20.png)
> davinci developer
> swc设计
> ![alt text](image-21.png)
> davinci configurator pro
> ![alt text](image-22.png)
> ![alt text](image-23.png)
> 附录
> ![alt text](image-24.png)
> 多核
> ![alt text](image-25.png)