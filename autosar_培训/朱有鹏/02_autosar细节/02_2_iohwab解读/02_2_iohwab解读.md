## 2.2 iohwab 模块解读
> 三大学习资料 (software architecture\ artic core源码、 iohwab文档)
> ![alt text](image.png)
> ![alt text](image-1.png)
> ![alt text](image-2.png)
### abstraction 
> 没有服务层，直接就是ECU抽象层
> 关心的是外设，不关心sensor和actuators
> 只是实现驱动
> 不同的IO设备，可能都通过同一个IO service访问
> ![alt text](image-4.png)
> ![alt text](image-3.png)
> ![alt text](image-5.png)
> 性质： mcu 独立 依赖ECU
> 任务：向更高层隐藏ECU板端性质
> ![alt text](image-6.png)
> #### .h文件
> DET: default error trace 开发时错误追踪
> ![alt text](image-7.png)
> #### .c文件
> ![alt text](image-9.png)
### IO文档
> IO中的Abstraction
> ![alt text](image-10.png)
> 目的：哪些swc与其相关，如何定义一个通用的port
> 不提供capi，不去管具体的功能域
> ![alt text](image-11.png)
> 简写
> ![alt text](image-12.png)
> 约束
> ![alt text](image-13.png)
> 可能用到的其他模块 （mcal \ comm(external..) \os也要具备能控制IO的能力）
> ![alt text](image-14.png)
> ![alt text](image-15.png)
> ECUM（init）\DET\BSW sche
> ![alt text](image-16.png)
> DCM （类似UDS）
> ![alt text](image-17.png)
> 7 功能描述
> API0 内部接口（不同厂家可能不一样）
> API2 autosar interface , api2是autosar规定的名字（不同厂家API2相互兼容）
> ![alt text](image-18.png)
> ![alt text](image-19.png)
> 案例
> ![alt text](image-20.png)
> ![alt text](image-21.png)
> ![alt text](image-22.png)
8 API 定义
> ![alt text](image-23.png)
> ![alt text](image-26.png)
> ![alt text](image-25.png)
> function
> ![alt text](image-27.png)
> callback notify
> ![alt text](image-28.png)
> 时序图
> 首先ECUM 发出ADCinit请求，经过IOHWAB,然后IOHWAB初始化，请求adc group notify 使能 
> ![alt text](image-29.png)
> 通知获取电压值
> ![alt text](image-30.png)
> ![alt text](image-31.png)
> 读取电压值
> ![alt text](image-32.png)

### io模块文档 sws
> 5 与其他模块的关联 mcu(内部时钟) port
> ![alt text](image-33.png)
> 7 function specification 错误定义
> ![alt text](image-34.png)
> ![alt text](image-35.png)
> 8 API specification API定义
> ![alt text](image-36.png)
> sequence diagram (各个函数定义的流程) 11种模式
> ![alt text](image-37.png)
> ![alt text](image-38.png)
> ![alt text](image-41.png)