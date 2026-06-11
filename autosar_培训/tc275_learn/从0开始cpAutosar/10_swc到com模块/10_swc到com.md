## 10 swc到com
> **10.1 com 模块介绍**
> 总共三个阶段
> 1）调用rte接口，将信号值存到buffer中，并且设置发送请求
> 2）com_mainfunctiontx检测到发送请求，调用下层接口，将报文发送出去
> 3）收到tx comfirmation
> ![alt text](image.png)
> **10.2 com 模块 实操**
> **发送第一阶段 swc和bsw配置**
> 进行data mapping，把data element和signal进行关联
> ![alt text](image-1.png)
> swc中关联dbc中的signal
> ![alt text](image-2.png)
> 创建port口（tx和rx）
> ![alt text](image-4.png)
> ![alt text](image-3.png)
> ![alt text](image-5.png)
> 在swc中创建 port interface 
> ![alt text](image-6.png)
> ![alt text](image-7.png)
> 在swc中指明runnable使用者
> ![alt text](image-8.png)
> ![alt text](image-9.png)
> 对port口配置（初始值，enable api用于生成rte接口）
> ![alt text](image-10.png)
> ![alt text](image-11.png)
> 在bsw层关联 （com层和swc层）
> ![alt text](image-13.png)
> ![alt text](image-14.png)
> swc代码中调用rte接口
> ![alt text](image-15.png)
> 还需要在bsw中配置com层ipdu发送模式
> 配置成direct模式
> 信号配置成triggered 模式
> ![alt text](image-16.png)
> ![alt text](image-17.png)
> **10.3操作讲解**
> 注释，delegation port就是在ecu composition层面的port
> ![alt text](image-18.png)
> 显式调用与隐式调用
> 显式调用，rte直接调用com_send
> 隐式调用是先存到buffer中，在task中调用com_sendsignal
> ![alt text](image-19.png)
> 配置选项，transfer property:
> triggered 是调用了com接口的话就会触发消息传输
> 配置决定是否会设置发送请求
> ![alt text](image-21.png)
> ![alt text](image-20.png)
> **10.4 tx filter实操**
> 分成两种发送模式 txModeTrue txModeFalse
> filter决定发送的模式（true mode false mode）具体是否发送，是由模式里配置的内容决定的
> 只要有一个signal为ture,message就是true的发送模式，signal全是false，则message才是false
> 因此每个signal发送都会有true和false
> ![alt text](image-23.png)
> ![alt text](image-22.png)
> ![alt text](image-24.png)
> com filter设置在0-2000之间
> ![alt text](image-25.png)
> 为了让false工况下也能发送出报文，因此修改txModeFalse
> ![alt text](image-26.png)
> ![alt text](image-27.png)
> 总结：第一阶段流程
> 调用rte服务函数，在rte里面调用com_sendsignal,评估filter,设置发送请求
> ![alt text](image-28.png)
> **10.5 com tx发送第二阶段**
> 发送第二阶段，主要是配置发送的mode
> direct,在下一次com_mainfuntiontx中传输消息，和number of repetitions搭配使用。表示trigger events触发后，又发了几次报文，
> ![alt text](image-29.png)
> periodic 周期性，在mainfunction中设置，time_offset和time period应为mainfunction 的整数倍
> ![alt text](image-30.png)
> ![alt text](image-31.png)
> 发送第二阶段总结
> ![alt text](image-32.png)
> 在调用pdur_comtransmit前调用callout函数，传入参数为pdu id和info,返回结果是true的情况下，才会调用pdur_comtransmit,很重要，可以自定义实现
> ![alt text](image-33.png)
> ![alt text](image-34.png)
> **10.6 com发送第三阶段**
> 每个signal都有一个notification,收到tx confirmation的时候就会调用这个notification函数
> 参数决定了在什么位置被调用
> ![alt text](image-35.png)
> **10.7 Com Rx阶段**
> com接收分为两个阶段
> 通过com_rxindication把数据存到buffer中
> swc通过rte接口读取信号值
> ![alt text](image-36.png)
> 接收第一阶段
> 调用com_rxindication后，先调用 ipdu allout函数，如果返回true，才进行后面的处理 
> ![alt text](image-38.png)
> Rx filter
> 用于确定接收事件是否转发给应用程序
> 只有满足filter，才把数据发送buffer中
> ![alt text](image-39.png)
> notification (deferred、immediate)
> ![alt text](image-40.png)
> 接收代码流程
> ![alt text](image-42.png)
> 接收第二阶段
> 有三种读取signal的方式，显性写，隐性写
> 默认选择explicit by argument
> ![alt text](image-44.png)
> ![alt text](image-45.png)