## UDS通用知识点 dcm
> 传统的uds服务
> ![alt text](image.png)
> 通用知识点
> ![alt text](image-1.png)
> **诊断请求**
> ![alt text](image-2.png)
> 诊断请求格式（有无子服务）
> ![alt text](image-3.png)
> ![alt text](image-5.png)
> 肯定响应
> ![alt text](image-4.png)
> si 服务id
> ![alt text](image-6.png)
> 否定响应
> ![alt text](image-7.png)
> ![alt text](image-8.png)
> ![alt text](image-9.png)
> 抑制肯定响应位（不需要肯定响应）
> 属于子服务参数的内容 （类似 19 01-> 19 81）,既没有肯定响应，也没有否定响应
> 没有子服务的不涉及
> ![alt text](image-10.png)
> ![alt text](image-11.png)
> 否定响应的NRC
> 0X12 子服务不支持 0x13 长度不正确  
> ![alt text](image-12.png)
> 不同服务要支持不同的NRC
> ![alt text](image-13.png)
> **nrc如何开发**
> ![alt text](image-14.png)
> nrc优先级
> ![alt text](image-15.png)
> 在判断nrc前后会有callout
> ![alt text](image-16.png)
> ![alt text](image-17.png)
> **dcm的一些概念 诊断通讯管理**
> 三个子模块
> dsd 诊断服务调度
> dsl 会话层
> dsp 处理层
> ![alt text](image-18.png)
> dcm autosar标准
> dsl->dsd->dsp
> ![alt text](image-19.png)