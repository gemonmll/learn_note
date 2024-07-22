## RTE
### rte
应用层和软件层之间 
![alt text](image.png)
rte 在swc和bsw 之间
![alt text](image-1.png)
### 架构
![alt text](image-2.png)
### rte功能 
> 类似vfb virtural funciont bus
> 数据传输
> ![alt text](image-3.png)
> 可执行实体的运行环境
> 把runable 配置到os、 配置触发方式 、调度配置项
> 完全是生成的
> ![alt text](image-4.png)
> rte可以调度的接口 （os,ecu-m,swc,com）
> ![alt text](image-5.png)
> rte触发runables的形式，初始化，timing,event
> ![alt text](image-6.png)
> rte作为通信接口
> ![alt text](image-7.png)
### inter ecu sender/receiver 通信
> ![alt text](image-8.png)
> 几种传输模式 direct 直接地址
> ![alt text](image-9.png)
> buffered ,last is best
> ![alt text](image-10.png)
> queued 队列
> ![alt text](image-11.png)
> data invalidation 数据失效形式
> ![alt text](image-12.png)
### client server communication
> 远程服务 同步调用 异步调用
> ![alt text](image-13.png)
> 同步调用 时序
> ![alt text](image-14.png)
> 异步调用 时序
> ![alt text](image-15.png)
### rte保护机制 intra-swc communication
> 保护数据一致性（原子操作）
> 1）专属区域保护 2）保护变量
> ![alt text](image-16.png)
### 三种接口定义
> 三种接口
> ![alt text](image-17.png)
> standardized interface(rte与bsw之间)
> ![alt text](image-18.png)
> autosar interface (rte和asw之间 用户自己定义的接口)
> port 和 runnable 描述
> ![alt text](image-19.png)
> standardized autosar interface(提供服务 services之间)
> ![alt text](image-20.png)
>  接口定义 
> ![alt text](image-21.png)
> ![alt text](image-22.png)
### rte生成代码过程
> ![alt text](image-23.png)