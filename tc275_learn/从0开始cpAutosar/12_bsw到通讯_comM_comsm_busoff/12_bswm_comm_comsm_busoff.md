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
> ### 3 comm
> status有三个：no com \silent com\full com （与bswm相关）
> 三个大状态下还有子状态 channel state
> silentcom 用户不能直接请求
> ![alt text](image-34.png)
> 相关变量（comm_userreqfullcom comm_activecommode comm_comallowed comm_buscommodereq comm_bussmstate）
> ![alt text](image-35.png)
> **内部处理过程**
> 内部处理过程
> 计算出最高的commode
> ![alt text](image-37.png)
> ![alt text](image-36.png)
> 真正模式切换的部分
> ![alt text](image-38.png)
> ![alt text](image-39.png)
> **与其他模块交互**
> 与swc的交互，通过rte连起来
> ![alt text](image-40.png)
> service port 服务接口
> ![alt text](image-41.png)
> 与bswm和cansm的交互
> ![alt text](image-42.png)
> ### 4 canSM
> cansm状态机 （fullcom prefullcom prenocom ..）
> ![alt text](image-43.png)
> cansm 状态变量（cansm_channelvarrecordc）
> ![alt text](image-44.png)
> ![alt text](image-45.png)
> ![alt text](image-46.png)
> ![alt text](image-47.png)
> cansm_universaltimer 用于保存一些时间参数
> ![alt text](image-49.png)
> ![alt text](image-48.png)
> lastvalidbaudrate 
> requestedcommode,对cansm请求的mode
> indicatedcommode,上次cansm上报comm的mode
> currentstate:非常重要，当前cansm的状态
> modeindicationresponsible，表明哪个function对cansm进行状态处理，必须等这个函数处理完了或nobody才能下个函数
> bswmindicatedstate和bswmnewstate,通知bswm新的状态
> busoff flag，busoff发生的次数
> **通讯控制相关处理流程**
> mainfunction,universaltimer为0后再进行状态切换
> ![alt text](image-50.png)
> cansm_checkmodeindication
> mode进行比对，上报给bswm
> ![alt text](image-51.png)
> 与其他模块的交互
> ![alt text](image-52.png)
> **演示 full com request流程**
> ![alt text](image-53.png)
> 断点调试 caninit函数 （no com 0x40）
> ![alt text](image-54.png)
> ![alt text](image-55.png)
> mainfunction中处理的地方
> ![alt text](image-56.png)
> ![alt text](image-57.png)
> 先屏蔽掉 fullcommution请求
> ![alt text](image-58.png)
> ![alt text](image-59.png)
> 没有请求full communication请求，稳定nocom 状态
> ![alt text](image-60.png)