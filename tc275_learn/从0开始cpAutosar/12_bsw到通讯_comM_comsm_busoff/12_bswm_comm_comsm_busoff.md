## 12 bswm_comm_comsm_busoff
> 通讯控制
> ![alt text](image.png)
> 通讯控制整体介绍
> swc请求 comm_requestcommode
> communication control功能打开
> ![alt text](image-1.png)
> ![alt text](image-2.png)
> ![alt text](image-3.png)
> 整体流程调用框图
> ![alt text](image-4.png)
> ### 1 canif com模块回顾
> **canif controller模式**
> 通过canif_setcontrollermode进行切换，切换后会调用canif_controllermodeindication来通知上层
> ![alt text](image-5.png)
> **canif pdu模式**
> 一般都是在set controller后，在indication中设置pdu模式
> ![alt text](image-7.png)
> ![alt text](image-6.png)
> **com模块 - ipdu group**
> 启用和禁用com ipdu的接收与传输
> ![alt text](image-8.png)
> ### 2 bswm和通讯控制相关内容介绍
> bswm_genericstate:用来存自己的状态和其他模块的情况
> pending request 有获取与使用的地方
> state存bswm自己的状态，即流程图的状态
> ![alt text](image-10.png)
> ![alt text](image-11.png)
> 第二个变量 bswm_commchannelstate,表示comm的状态，只有是nocom的状态，才能退出run状态
> ![alt text](image-12.png)
> cansm发出模式切换后，在indicatioN中告知comm,并存到comm_bussmstate,告知不是nocom，只有是nocom,才能从run到postrun
> ![alt text](image-14.png)
> **配置工具**
> 判断是否有pending request
> ![alt text](image-15.png)
> **action list**
> condition,每次评估规则时都执行操作列表
> trigger，每次评估结果发生变化时都执行动作列表
> ![alt text](image-16.png)
> ![alt text](image-17.png)
> **bswM和通讯之间的影响**
> **communication control**
> 勾选操作的意义
> ![alt text](image-19.png)
> ![alt text](image-18.png)
> 主要是bswm和cansm之间关联的过程
> 如果ipdu是关闭的情况下，则根据action不会发送
> 勾选的目的是打开ipdu
> rx_dm (deadline monitoring)
> ![alt text](image-21.png)
> ![alt text](image-20.png)
> ![alt text](image-22.png)
> ![alt text](image-23.png)
> 疑问点
> ![alt text](image-24.png)
> ![alt text](image-25.png)
> **support comm**
> ![alt text](image-26.png)
> ![alt text](image-27.png)
> wakeup to run 条件
> ![alt text](image-28.png)
> comm allow action
> 告诉comm可以进行通讯
> ![alt text](image-29.png)
> **comm和bsw之间的影响**
> ![alt text](image-30.png)
> pending request 和 commchannelstate 表示com状态
> ![alt text](image-31.png)
> cansm和bswm间也有参数会开启关闭ipdu group
> ![alt text](image-32.png)
> ![alt text](image-33.png)