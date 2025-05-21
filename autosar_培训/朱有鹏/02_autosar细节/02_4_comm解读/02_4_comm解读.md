### 4 comm模块
#### 4.1 综述
> 整体目录
> ![alt text](image.png)
> 分层结构 有线和无线（很多融合在一起）
> ![alt text](image-1.png)
> service层 很多（重点关注 PDU SM(state manager) NM(newwork manager) ）
> ![alt text](image-2.png)
> ![alt text](image-3.png)
> 当Hardware固定为CAN时的架构图
>  ![alt text](image-4.png)
> 文档大致分类
> ![alt text](image-6.png)
> ![alt text](image-7.png)
> com层
> ![alt text](image-8.png)
> ![alt text](image-9.png)
#### 4.2 功能模块简介
> com层 对上的封装
> PDU: protocal data unit 协议数据单元（类似payload 有效数据）
> can/lin/flexray/eth/v2x/wireless 通讯总线
> J1939 通讯有关上层通讯协议
> TTCAN 扩展CAN 可选
> Diagnostic 诊断 UDS(通过通信来实现的) DoCan DoIP
> Transformer: 格式转换
> NM/SM 网络管理 状态管理
> SecOC: 通信安全
> SomeIP: 应用层通信协议
> TP: 传输层协议（中间层适配，网络层与物理层之间，如果数据量小就可以不需要tp层）
#### 4.3 COM模块解读 (对上对接)
> 目录
> ![alt text](image-10.png)
> com分为两个部分 
> comm只是来管理,也会与SWC会有一些状态的交互 数据管理
>  autosarcom用来上下对接（signals IPDU） 数据通信
> ![alt text](image-11.png)
> ![alt text](image-12.png)
> 文档 com_sws
> ![alt text](image-13.png)
> 第一章概览
> 把signal打包成ipdu
> ![alt text](image-14.png)
> 缩略语
> ![alt text](image-15.png)
> 主要关注api和sequence diagram
> ![alt text](image-16.png)
> 定义了些回调函数给别人调用
> ![alt text](image-17.png)
> 需求文档对应函数设计
> ![alt text](image-18.png)
#### comm 模块
> comm 函数调用
> ![alt text](image-19.png)
> comm和dcm ecum之间都有关联
> ![alt text](image-20.png)
> 一些时序图
> pdur调用了COM的callback接口
> ![alt text](image-21.png)
> ![alt text](image-22.png)
> 调用com的callback
> ![alt text](image-23.png)
> pdur rte com之间的交互 文档理解
> ![alt text](image-24.png)

### 5 NM模块
> 管理休眠模式和工作模式之间的切换
> ![alt text](image-25.png)
> 缩略语
> ![alt text](image-26.png)
> 如何查看函数
> ![alt text](image-27.png)
> ![alt text](image-28.png)
> 重点是通过SRS来设计函数
> ![alt text](image-29.png)
> ![alt text](image-30.png)
>
### 6 cansm和diagnostic
> cansm can总线状态（切换）的管理（空闲 通信）
> ![alt text](image-31.png)
> ![alt text](image-32.png)
> 实现控制流
> ![alt text](image-33.png)
> 函数执行
> ![alt text](image-34.png)
> ![alt text](image-35.png)
> 时序图
> ![alt text](image-36.png)
> #### diagnostic
> 很重要 诊断 分为两个部分
> （DLT 位于COM内部
> /DEM DCM DET 与COM 并列 （UDS诊断）
> ![alt text](image-39.png)
> ![alt text](image-37.png)
> ![alt text](image-38.png)
> ![alt text](image-40.png)
> ![alt text](image-41.png)
> ![alt text](image-42.png)
> ![alt text](image-43.png)
> ![alt text](image-44.png)
> ![alt text](image-45.png)
> 时序图
> ![alt text](image-46.png)
### 7  剩余模块
> ![alt text](image-47.png)
> eth 
> ![alt text](image-48.png)
> layout arch
> ![alt text](image-49.png)
> J1939
> ![alt text](image-50.png)
> pdu (ISO标准 非autosar标准)
> ![alt text](image-51.png)
> secoc 数据加密认证
> ![alt text](image-52.png)
> ![alt text](image-53.png)
> transformer 只是对数据处理 数据签名
> ![alt text](image-54.png)
> ![alt text](image-55.png)
### 8 总结
> 复杂度很高，深度可以先不需要太深，需要合理的切割
> autosar 是执行层面的方法论
> 从srs到sws,平衡全局架构和局部细节
> ![alt text](image-56.png)