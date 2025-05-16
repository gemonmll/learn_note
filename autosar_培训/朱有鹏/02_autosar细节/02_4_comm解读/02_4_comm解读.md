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
> 