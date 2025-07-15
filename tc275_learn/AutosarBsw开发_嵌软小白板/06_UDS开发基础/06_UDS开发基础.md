## BSW开发基础
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