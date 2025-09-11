## 新增一路can通道
> 需求描述
> ![alt text](image-21.png)
> 配置dbc,若是ilsupport选择no,则在com层不会生成配置
> ![alt text](image-22.png)
> 多个dbc需要选择相同的节点名字，否则无法next
> ![alt text](image-23.png)
> 配置can控制器 删除NM（不需要网络管理）
> ![alt text](image-24.png)
> comm 整车can配置成full 内部can配置成none
> nm 去掉passive mode
> ![alt text](image-25.png)
> ![alt text](image-26.png)
> ![alt text](image-27.png)
> 由于没有ilsupport，因此canif不会与com交互
> ![alt text](image-28.png)
> 上层模块选择cdd (自定义)
> ![alt text](image-29.png)
> 在cdd模块中关联ecuc的缓存
> ![alt text](image-30.png)
> 配置新通道的task mapping 
> ![alt text](image-31.png)
> bswm配置，allow comm
> ![alt text](image-32.png)
> ![alt text](image-33.png)
> **额外，通过kl15控制comm状态，full com,no com**
> ![alt text](image-34.png)
> 让内部can一直处于保持通讯的状态
> 新增一个从wakeupToRun下的full com 请求
> ![alt text](image-35.png)
> ![alt text](image-36.png)
> **硬件EB配置**
> davinci工具中没有tcan1042,因此需要在eb中配置port口，对于整车can,cantrcv有1043收发器模块，可以在davinci中配置
> ![alt text](image-38.png)
> ![alt text](image-37.png)
> 配置port 口
> ![alt text](image-39.png)
> ![alt text](image-40.png)
> **cdd 文件添加cbk**
> ![alt text](image-41.png)
> **测试过程**
> 配置下canif的接收范围
> ![alt text](image-42.png)
> ![alt text](image-43.png)
> ![alt text](image-44.png)
> 配置后可以正常接收
> ![alt text](image-45.png)
> **发送一路配置**
> 在canif_cfg中找到对应的canid
> ![alt text](image-47.png)
> 调用canif模块发送出去
> ![alt text](image-48.png)
> ![alt text](image-49.png)