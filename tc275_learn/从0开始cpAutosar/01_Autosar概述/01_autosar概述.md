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
> os application (tasks ISRs Alarms CounterS)集合
> 同一个OS Application可以互相访问，不同需要授权
> 一个核中可以有多个，一般来说配两个就行（systemApplication,用户使用的OsApplication）
> 