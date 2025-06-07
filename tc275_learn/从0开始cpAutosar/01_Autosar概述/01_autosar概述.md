### 01 Autosar概述
> Autosar概述
> 一套文档，一个框架 一个方法论
> ![alt text](image.png)
> 环境搭建
> ![alt text](image-1.png)
> eb环境（mcal）集成到vector中
> ![alt text](image-2.png)
> 最小系统的搭建
> ![alt text](image-3.png)
### 02 最小工程介绍
> ![alt text](image-4.png)
> 最小系统需要的模块
> ![alt text](image-5.png)
> #### 2.1 OS详解
> os介绍
> os存在 sc1 sc2 sc3等级
> ![alt text](image-7.png)
> os application (tasks ISRs Alarms CounterS)集合 类似用户组
> 同一个OS Application可以互相访问，不同需要授权
> 一个核中可以有多个，一般来说配两个就行（systemApplication,用户使用的OsApplication）
> app内访问使用RTE，app间访问用IOC(inter-osApp-comm),ecu间访问使用Com
> ![alt text](image-8.png)
> ### 2.2 task (bcc ecc)
> bcc 与 ecc, 多了wait状态
> 注意bcc是terminateTask
> ecc是waitEvent(while 1 循环)
> ![alt text](image-9.png)
> ![alt text](image-10.png)
> bcc1和ecc1的区别
> bcc1是不可抢占任务，但ecc1是取决于配置
> ![alt text](image-11.png)
> ### 2.3 tick Counter Alarm
> systemTimer 配置计算
> 软件中断和硬件中断
> ![alt text](image-12.png)
> 一个counter 可以关联多个Alarm
> 但一个alarm只会触发一个task
> 激活task,setEvent,调用callback
> ![alt text](image-13.png)
> scheTable可以看作是Alarm的升级版