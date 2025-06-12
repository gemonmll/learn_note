## CAN协议栈配置与调试
> ### 1 协议栈基础
> CAN协议栈 黑色数据流 黄色控制流
> ![alt text](image.png)
> 整体介绍 PDUR负责报文的路由转发
> ![alt text](image-1.png)
> API调用关系
> 发送成功后会触发Tx中断，从下到上再传回txconfirmation信息
> ![alt text](image-3.png)
> com->pudr->canif->can
> ![alt text](image-4.png)
> 接收链路 中断中处理
> ![alt text](image-5.png)
> ### 2 配置协议栈
> ecuc中是全局的pdu
> 通过pdur判断目标pdu和源pdu
> ![alt text](image-6.png)
> 对can总线进行配置
> ![alt text](image-7.png)
> 配置EN DIO
> ![alt text](image-8.png)
> 配置CAN port 引脚 还有rxsel寄存器
> ![alt text](image-9.png)
> ![alt text](image-10.png)
> ![alt text](image-11.png)
> 找到CAN00在davinci cfg所对应的名字
> ![alt text](image-12.png)
> ![alt text](image-13.png)
> ![alt text](image-14.png)
> 配置CAN时钟源
> ![alt text](image-15.png)
> 配置CAN 波特率
> ![alt text](image-16.png)
> ![alt text](image-17.png)
> 配置CAN FD support
> ![alt text](image-18.png)
> CAN general 时钟源选择
> ![alt text](image-19.png)
> ![alt text](image-20.png)
> 选择base can0
> ![alt text](image-21.png)
> ![alt text](image-22.png)
> 选择任务mapping
> ![alt text](image-23.png)
> 配置中断
> bus controller
> ![alt text](image-25.png)
> 中断形式
> ![alt text](image-24.png)
> 配置中断号
> ![alt text](image-26.png)
> ![alt text](image-27.png)
> init 
> ![alt text](image-28.png)
> ### 3 调试CAN协议栈
> 调试排查思路
> ![alt text](image-42.png)
> 配置编译工具
> ![alt text](image-29.png)
> 缺少network 文件
> ![alt text](image-30.png)
> ![alt text](image-31.png)
> 在rte_types中添加头文件
> ![alt text](image-32.png)
> configure工具中设置周期性发送
> ![alt text](image-33.png)
> ![alt text](image-39.png)
> ![alt text](image-40.png)
> 依旧没有报文，是需要报文状态管理
> ![alt text](image-34.png)
> comm_requestSm没有调用
> ![alt text](image-35.png)
> 把服务接口连接到新的接口
> 请求requestsm服务 full communication
> ![alt text](image-36.png)
> ![alt text](image-37.png)
> ![alt text](image-38.png)
> 配置初始化
> ![alt text](image-41.png)
> 调试后发现pdu没打开
> 打开配置
> ![alt text](image-43.png)
> ![alt text](image-44.png)
> 出现det问题
> ![alt text](image-46.png)
> OS_STATUS_DISABLEINT
> 调用函数时中断不应该是屏蔽状态
> 解决方法，不适用loopchek功能，或不使用os counter 或临界区不屏蔽全局中断
> ![alt text](image-47.png)
> ![alt text](image-48.png)
> ![alt text](image-49.png)
> hardware loop check功能
> 启用硬件循环检查以避免无限循环
> ![alt text](image-50.png)
> disableInterrupt/enableInterrupt,和suspendalInterrupt,resumeInterrupt的区别
> ![alt text](image-51.png)
> ![alt text](image-52.png)
> ![alt text](image-53.png)
> 屏蔽全局中断，启动自定义的ea配置
> ![alt text](image-54.png)
> ![alt text](image-55.png)
> 配置结果
> 发送报文
> ![alt text](image-45.png)
> 接收报文 （在中断中处理，rxIndication）
> ![alt text](image-56.png)
> RTE中没有 Com_ReceiveSignal()的原因是没进行data mapping
> ![alt text](image-57.png)

