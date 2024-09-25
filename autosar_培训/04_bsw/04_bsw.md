## BSW
> BSW部分
> 包括service layer\ ecu abstraction \ microcontroller abstraction layer
> ![alt text](image.png)
### service layer
> L型，一部分直接与mic相连(os,诊断，comm,nvm...)
> ![alt text](image-1.png)
### ecu abstraction layer
> driver
> ![alt text](image-2.png)
### microcontroller abstraction layer
> 硬件厂商提供
> ![alt text](image-3.png)
### cdd 
> 自定义， 复杂驱动，复杂执行器
> ![alt text](image-4.png)
### 模块细节定义
> system memory comm
> ![alt text](image-5.png)
> osek 软件架构 can ecu
> ![alt text](image-6.png)
> autosar架构
> ![alt text](image-7.png)
### bsw各个模块的功能
> 1 通信 communication 内部通信
> ![alt text](image-8.png)
> 说明
> ![alt text](image-9.png)
> 具体例子
> send
> ![alt text](image-10.png)
> receive
> ![alt text](image-11.png)
> 
> 2 mode management 模式管理
> 状态管理 处理ecu基本状态 sleep 等等
> 总线网络管理 network management 保持唤醒
> bsw状态管理 rule based
> ![alt text](image-12.png)
>
> 3 watchdog 看门狗
> ![alt text](image-13.png)
>
> 4 存储服务
> ![alt text](image-14.png)
> 例子
> ![alt text](image-15.png)
>
> 5 诊断服务
> dcm(诊断协议)  dem(dtc处理 错误内存) fim
> ![alt text](image-16.png)
> 例子
> ![alt text](image-17.png)
>
> 6 hardware io 与传感器交互
> ![alt text](image-18.png)
> 例子
> ![alt text](image-19.png)