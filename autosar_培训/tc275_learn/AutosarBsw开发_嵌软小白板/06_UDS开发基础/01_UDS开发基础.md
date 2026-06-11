## UDS开发基础
### 1 基础
> 目录
> ![alt text](image.png)
> 基本概念，university diagnostics system
> ![alt text](image-1.png)
> ![alt text](image-2.png)
> 诊断报文 （物理请求报文、功能请求报文、响应报文）
> 功能请求报文不支持多帧、NRC11\12\31\73\7F不反馈
> ![alt text](image-3.png)
> ![alt text](image-4.png)
> ![alt text](image-5.png)
> UDS on Can(也可以用于以太网和lin)
> ![alt text](image-6.png)
> ![alt text](image-7.png)
> ![alt text](image-8.png)
> UDS服务
> ![alt text](image-9.png)
> UDS需求
> 需要车企提供，有很多定制化需求（比如车速<10km，才能reset）
> ![alt text](image-10.png)
> ![alt text](image-11.png)
> ### 2 配置CAN诊断报文链路
> 需求
> ![alt text](image-12.png)
> 首先更新dbc，注意属性 diagRequest 物理诊断报文
> ISO-TP对应15765
> ![alt text](image-13.png)
> ![alt text](image-14.png)
> 先配置can canif
> ![alt text](image-15.png)
> CANTP 参数配置（偏大无影响，偏小容易超时）
> ![alt text](image-16.png)
> **配置链路注意点**
> CANIF indication UL->CANTP
> ![alt text](image-17.png)
> ![alt text](image-18.png)
> 对于周期应用报文，下一个周期会继续发送报文，与当前发送是否成功无关，因此不需要 TX Confirm
> ![alt text](image-19.png)
> 对于诊断报文，涉及到多帧传输，需要诊断报文TxConfirm获取发送状态
> ![alt text](image-20.png)
> 对于事件型报文，也需要Tx confirm
> ![alt text](image-21.png)
> DCMdslbuffer（dem处理好后，填到dcm中），通过dcm发送出去
> ![alt text](image-22.png)
> ![alt text](image-23.png)
> 正常响应（物理请求 功能请求）
> ![alt text](image-24.png)
> ### 3 诊断传输协议详解
> 以一个服务为例子 19服务 DTC （子服务01 子服务0a）
> **请求格式**
> 01:根据dtc掩码返回dtc数量
> ![alt text](image-30.png)
> **响应格式**
> ![alt text](image-25.png)
> ![alt text](image-26.png)
> 第二个字节请求01返回也是01
> 第三个字节是dtc状态掩码，也是DTC的状态位
> 第四个字节是dtc形式 01(14229)
> 第五第六表示支持DTC的数量
> ![alt text](image-29.png)
> DTC的状态掩码实际上是DTC的状态位，第一位和第三位是强制的
> ![alt text](image-28.png)
> **请求响应示例**
> 19 01 01 返回第一位是1的dtc码的数量
> ![alt text](image-31.png)
> 有两个置位的dtc
> ![alt text](image-32.png)
> **0A子服务**
> 0A服务获取所有dtc及dtc对应的状态掩码
> ![alt text](image-33.png)
> 返回了全部的DTC
> ![alt text](image-34.png)
> ![alt text](image-35.png)
> **15765-2 tp层协议**
> 单帧
> ![alt text](image-37.png)
> ![alt text](image-36.png)
> 首帧 连续帧 流控帧
> ![alt text](image-39.png)
> 流控帧 FC
> ![alt text](image-40.png)
> ![alt text](image-41.png)
> 将bs值设置为1后的现象
> ![alt text](image-42.png)
> stmin表示发送的事件
> 连续帧
> ![alt text](image-43.png)
> **一些配置项**
> padding pattern
> ![alt text](image-44.png)
> **注意事项 canfd和can的tp协议是不同的**
> 普通can协议和canfd协议的tp协议是不同的
> 如果是canfd发03 190101的话
> 则要发 00 03 19 01 01 头一个字节需要是00
> ![alt text](image-45.png)
