## pdur 模块
> 模块简介
> 将上层和下层联系起来，不对数据进行处理，只是进行转发，只有src pdu 和 dst pdu
> 起到网关作用
> ![alt text](image.png)
> #### 模块实操
> 新配置一路can
> 现在canif上新增一路can
> ![alt text](image-1.png)
> 在ecuc中创建一个全局pdu
> ![alt text](image-2.png)
> canif关联ecuc 中的全局pdu
> ![alt text](image-3.png)
> 之后pdur中 destination中关联新的pdu
> ![alt text](image-4.png)
> ![alt text](image-5.png)
> 新建一个pdu des 关联到新发的pdu中
> ![alt text](image-6.png)
> 启用gateway功能
> ![alt text](image-7.png)
> 结果
> ![alt text](image-8.png)
> #### 配置梳理
> 项目总体梳理
> ![alt text](image-9.png)
> #### 配置详细介绍
> 数据处理的方式 data processing
> immediate 就是在当前的函数中执行路由（中断）
> deffered 在下一个mainfunction中执行路由
> dat prowivision:direct 由pdur调用复制pdu、triggerTransmit 由调用模块（canif）调用，这种配置能够使用最新的数据，需要配置single buffer
> ![alt text](image-11.png)
> ![alt text](image-10.png)
> pdu 长度处理，如果收到的pdu比配置的大，处理方式（丢弃，缩短）
> ![alt text](image-12.png)
>> 数据量比较多的情况下需要用到buffer，比如诊断数据，配到queue
> ![alt text](image-13.png)
>> queue的配置（shared buffer）
>> ![alt text](image-14.png)
>> ![alt text](image-16.png)
>> txbuffer新建
>> ![alt text](image-15.png)
>> 关联到queue中
>> ![alt text](image-17.png)
> #### 配置详细介绍
> **pdur queue的类型**
> single buffer :last is best，只会更新最新的数据
> ![alt text](image-18.png)
> ![alt text](image-19.png)
> **queue的配置**
> depth参数配置
> to thresholde ：参数非常重要，需要等到source的数据全部接收后，才传给dest,只给tp层的参数
> buffer ref：显性 隐性
> ![alt text](image-20.png)
> ![alt text](image-21.png)
> **general 通用的一些配置**
> queue overflow notification ，发生了overflow，即buffer满了调用这个接口
> switching,动态ram表，动态路由配置
> ![alt text](image-22.png)
> ![alt text](image-22.png)
> **pdu中routing paths 可以看到路由关系**
> ![alt text](image-23.png)

