## 1 认识Autosar网络管理状态机
> 目录
> 状态详解(bussleep /repeat msg state/normal ope state/ ready sleep state/ prepare bus sleep)
> repeat message
> 诊断请求
> ![alt text](image.png)
> **1 状态管理详解**
> 一共五个状态
> ![alt text](image-1.png)
> autosar 网络管理详细的规范
> ![alt text](image-2.png)
> ![alt text](image-3.png)
> **bus sleep Mode**
> ![alt text](image-4.png)
> **repeat Msg state**
> 蓝色是非主流的路线
> ![alt text](image-5.png)
> 休眠到repeat
> 条件1 （网络需求：主动唤醒 网管报文：被动唤醒）
> action1,2 启动repeat_msg定时器
> action4 启动传送网络管理报文
> ![alt text](image-6.png)
> repeat 到 work
> 主动请求（网络请求）且定时器超时：
> action:发送网管报文
> ![alt text](image-7.png)
> 主动请求路线
> ![alt text](image-8.png)
> repeat -> 准备休眠
> 定时器超时
> action 停止发送网络报文管理
> ![alt text](image-9.png)
> 网络释放过程
> ![alt text](image-10.png)
> **Normal Operation State**
> 正常工作状态的跳转
> ![alt text](image-11.png)
> 正常到准备休眠
> 条件：网络释放（kl15）
> aciton5:节点停止发送报文
> ![alt text](image-12.png)
> 准备休眠到正常
> ![alt text](image-13.png)
> **ready sleep state**
> ![alt text](image-14.png)
> 准备休眠状态，到总线预休眠
> ![alt text](image-15.png)
> 接收到报文时就会刷新状态
> ![alt text](image-16.png)
> 主动唤醒，断开唤醒流程
> ![alt text](image-17.png)
> **prepare bus-sleep mode**
> ![alt text](image-18.png)
> 预休眠到休眠
> ![alt text](image-19.png)
> 预休眠到repeat
> ![alt text](image-20.png)
> ### 2 repeat Messag request
> 网管报文
> ![alt text](image-21.png)
> 网络管理帧
> 主要用到的是bit0和bit4
> ![alt text](image-22.png)
> ![alt text](image-23.png)
> ![alt text](image-24.png)
> ![alt text](image-25.png)
> 注意网络管理的状态
> 当收到重复消息请求位置为1时，都要往重复消息状态跳转，网络管理重复消息需求
> 在重复消息状态时ecu就会向外发网管报文，也会收到外部的网络管理帧，用来检测总线当前的网络节点
> ![alt text](image-26.png)
> ### 3 诊断请求
> 诊断请求可以理解为主动请求，但不是主动唤醒源
> ![alt text](image-27.png)
> **autosar 接口**
> 应用侧来检测，请求com_mode释放网络
> ![alt text](image-28.png)
> ### 4 网络管理需求规范
> 关键条件
> ![alt text](image-29.png)
> user data 0  填写唤醒源
> ![alt text](image-30.png)
> ![alt text](image-31.png)
> ![alt text](image-32.png)
> **正常操作状态和休眠**
> ![alt text](image-33.png)
> **各个状态的报文收发**
> ![alt text](image-34.png)
> **网络需求和网络释放**
> ![alt text](image-35.png)
> ### 5 实际开发配置
> 配置can filter
> ![alt text](image-36.png)
> dbc更改报文属性
> ![alt text](image-37.png)
> ![alt text](image-38.png)
> 配置参数
> ![alt text](image-39.png)
> 配置使能参数
> ![alt text](image-40.png)
> ![alt text](image-41.png)
> ![alt text](image-42.png)
> 初始化需求
> 再callout函数中完成
> ![alt text](image-43.png)
> ![alt text](image-44.png)
> ![alt text](image-45.png)
> 新的需求
> ![alt text](image-46.png)
> ![alt text](image-47.png)
> nm配置节点ID
> ![alt text](image-48.png)
> ![alt text](image-49.png)
> ### 6 网络管理测试
> 关注这个测试规范
> ![alt text](image-50.png)
> 测试举例
> ![alt text](image-51.png)
> ![alt text](image-52.png)
> 注意测试方法和验收标准
> ![alt text](image-53.png)
> 测试举例
> ![alt text](image-54.png)
> ![alt text](image-55.png)