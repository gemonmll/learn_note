## someip 协议介绍
> 目录
> ![alt text](image.png)
> SOA相关概念 soa与someip
> ![alt text](image-1.png)
> ![alt text](image-2.png)
### 1 概述
> ![alt text](image-3.png)
> 背景
> ![alt text](image-4.png)
> ![alt text](image-5.png)
> ![alt text](image-6.png)
> ![alt text](image-7.png)
> 功能 序列化 RPC SD 订阅发布 UDP分段
> ![alt text](image-8.png)
> 服务接口
> method 获取功能 发送请求
> property/field set/get方法操作成员变量
> event 事件 通知
> ![alt text](image-9.png)
> method RR FF
> Request/Response
> Fire/Forget
> ![alt text](image-10.png)
> Event 订阅服务 发布服务
> ![alt text](image-11.png)
> Field(属性、状态)
> ![alt text](image-12.png)
> 服务接口总结
> ![alt text](image-13.png)
> 服务接口实例
> ![alt text](image-14.png)
### 2 some/ip 报文
> 目录
> ![alt text](image-15.png)
> someip报文格式
> ![alt text](image-16.png)
> 报头 payload
> ![alt text](image-17.png)
> 报文唯一标识符
> ![alt text](image-19.png)
> length范围
> ![alt text](image-20.png)
> request ID (client id \ session id)
> ![alt text](image-21.png)
> ![alt text](image-22.png)
> protocal version 协议版本
> ![alt text](image-23.png)
> 接口版本 一致性检测
> ![alt text](image-24.png)
> message type 重点
> ![alt text](image-25.png)
> return code 
> ![alt text](image-26.png)
> ![alt text](image-27.png)

### 3 someip 序列化
> 序列化 反序列化
> ![alt text](image-28.png)
> ![alt text](image-29.png)
> 定义传输数据的字节序
> ![alt text](image-30.png)
> 序列化规则
> 结构体序列化 顺序排布 也可以增加length field
> ![alt text](image-31.png)
> 字符串序列化
> ![alt text](image-32.png)
> 动态长度string 在前面加上length
> ![alt text](image-33.png)
> Array 序列化
> ![alt text](image-34.png)
> 变长数据序列化
> ![alt text](image-35.png)
> ###  someip 报文示例
> ![alt text](image-36.png)
### 4 someip SD
> 服务寻址 事件订阅 两种功能
> ![alt text](image-37.png)
> ### someip sd 报文格式
> payload字段 messageid 固定
> ![alt text](image-38.png)
> flags字段
> ![alt text](image-39.png)
> entry arrays(事件寻址报文 事件订阅报文)
> ![alt text](image-40.png)
> service entry 字段
> ![alt text](image-41.png)
> 也可以携带一些额外信息
> ![alt text](image-42.png)
> ### 示例
> ![alt text](image-44.png)
> service ID 和 instance ID
> 实例是一个服务的具体实现
> ![alt text](image-45.png)
> ![alt text](image-46.png)
> ### 事件组 entry eventgroup entry
> ![alt text](image-47.png)
> ![alt text](image-48.png)
> option 内容
> ![alt text](image-49.png)
> ![alt text](image-50.png)
> endpoint option server端端口号 联系方式
> ![alt text](image-51.png)
> sd endpoint option
> ![alt text](image-52.png)
> configuration option
> ![alt text](image-53.png)
> load balancing option
> ![alt text](image-54.png)
> ### 示例
> 发现 0x1001服务
> 提供 ipv4 endpoint option
> ![alt text](image-55.png)
>
> ### 5 SD启动时序
> 服务端阶段
> ![alt text](image-57.png)
> 客户端行为
> ![alt text](image-58.png)