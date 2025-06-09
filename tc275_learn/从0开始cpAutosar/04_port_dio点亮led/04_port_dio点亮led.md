## 04  port dio 点亮led
> ### 4.1 对port引脚配置
> 主要关注三个属性
> 引脚方向、引脚电平、引脚功能
> ![alt text](image.png)
> ### 4.2 dio 模块
> port driver中没有给出控制引脚电平的API函数，当需要对引脚的电平进行操作时，需要通过DIO来实现
> 主要关注  dio port id和dio channel id
> ![alt text](image-3.png)
> 特别注意函数中调用的channelId是配置中两个id的组合
> channelid 是 dio_channel_2_5
> ![alt text](image-2.png)
> ### 4.3 实操部分
> ![alt text](image-4.png)
> mcal 配置
> ![alt text](image-5.png)
> davinci配置port和dio
> ![alt text](image-6.png)
> ![alt text](image-7.png)
> 配置初始化
> ![alt text](image-8.png)
> developer中配置1s的任务
> ![alt text](image-9.png)
> bsw中添加task mapping 和 alarm
> ![alt text](image-10.png)
> ![alt text](image-11.png)
> swc中添加代码
> DIO autosar资料 sws
> ![alt text](image-12.png)
> ![alt text](image-14.png)
> ![alt text](image-13.png)
> 编译配置中打开 dio
> ![alt text](image-15.png)