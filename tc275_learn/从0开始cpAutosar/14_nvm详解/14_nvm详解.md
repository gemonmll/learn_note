## NVM详解 
> ### NVM模块理论介绍
> 四种block：
> nv block 要存到nvm中的block,通过fee的flash
> \ram block 存到ram中的block，是app和nvm block共享的数据
> \ rom block 存在flash中，用于恢复
> \ admin block 包含nvram bloxk 所必须的ram数据
> ![alt text](image.png)
> **block状态跳转**
> nvm_blockmngmtarea nvramattributes
> bit0代表是否valid
> bit1代表是否changed
> bit4代表是否lock
> ![alt text](image-1.png)
> valid和change状态（只是ram block的状态）
> read block后，状态从Invalid转为valid,(保证了ram block和nv block一致)
> 也可以通过api手动更新
> ![alt text](image-2.png)
> ![alt text](image-3.png)
> lock状态
> 通常被dcm模块调用，防止被swc调用
> 如果锁定，写的时候，则此block id对应的nv内容不会被后续写入请求修改
> wrIteall会跳过这个块
> read all期间，无论状态如何，都会从nv memory中加载内容到锁定的nvram
> 通过setblock protection 设置写保护
> ![alt text](image-4.png)
> **management type**
> native,redundant(冗余)，需要fee中再加一个nvblock块,dataset
> ![alt text](image-5.png)
> ![alt text](image-6.png)
> **configuration class**
> 可以被调用的api接口，一般都采用class 3
> geterrorstatus:重要的信息，获取block的信息状态
> eraseNvBlock 只有优先级为0的block可以被擦除
> ![alt text](image-7.png)
> 重要的api
> Nvm_setramblockstatus，设置ram block的valid和changed状态 ，true表示ram已经更改，并计算ram的crc,在writeall期间写入。
> repairredundantblocks，检查冗余block，尝试通过有效block写入缺陷block
> ![alt text](image-8.png)
> writeBlock\readBlock 注意有没有ram block的配置
> 设置ram block后，传递空指针后，也是更新ram中的内容
> ![alt text](image-9.png)
> **优先级**
> 没打开优先级的话，是通过队列的形式，先进先出
> 多块请求优先级很低的job
> 对相同block id的读写操作，算一个job
> ![alt text](image-11.png)
> ![alt text](image-12.png)
> ![alt text](image-13.png)
> ![alt text](image-10.png)
> **同步请求**
> 调用时立即执行
> ![alt text](image-14.png)
> **异步请求**
> 有mainfunction参与,最主要区别
> polling方式的异步调用
> write_block只是写一些标志
> 在nvm_mainfunction中进行任务处理
> ![alt text](image-15.png)
> callback方式的异步调用
> ![alt text](image-16.png)
> **cancel流程**
> ![alt text](image-17.png)
> **readall流程**
> 会在初始化阶段调用一次
> ![alt text](image-18.png)
> ![alt text](image-19.png)
> block id为1的block ,（自动配置的block） nvm configure
> 代表 nvm memory layout的编号，自动配置，必须打开crc
> ![alt text](image-20.png)
> **nvm配置更新问题**
> 改变compiled configuration id 的值，启用动态配置信息，不抵制配置更改,readall后再进行writeall 尽量发生切页动作
> ![alt text](image-21.png)
> **writeall**
> 下电过程中调用writeall，把所有的值写入
> 确保id为1的block是最后处理的block
> 注意cancel writeall和kill writeall
> ![alt text](image-22.png)
> **cancel wirteall 时间过长的问题**
> 在cancel中配置超时时间，时间到了自动kill writeall
> ![alt text](image-23.png)
> ![alt text](image-24.png)
> 进行计时
> ![alt text](image-25.png)
> **nvm crc**
> 可以配置crc16和crc32
> nvm将数据和crc一起传给fee
> fee中的data数据是nvm的data和crc的结合
> mainfunction的crc计算 异步完成
> ![alt text](image-28.png)
> ![alt text](image-26.png)
> ![alt text](image-27.png)
> **crc 放的位置**
> 配置项为false的情况下需要流出crc内存的量
> 建议这个配置项一定要打开
> ![alt text](image-29.png)
> ![alt text](image-30.png)
> **crc处理的能力**
> 可以处理的最大字节数
> ![alt text](image-31.png)
> **crc compare mechanism**
> 打开功能后，nvm会保存成功读写操作的crc值并存到变量blockname_compcrc中
> 可以根据crc的值判断是否发生变化，是否需要执行存操作
> 减少不必要的写
> ![alt text](image-32.png)
> ![alt text](image-33.png)
> **calculate ram block crc**
> 比较各个位置的crc，减少readall期间的时间
> 减少不必要的读
> ![alt text](image-34.png)
> **数据加密**
> 使用csm数据加密与解密
> ![alt text](image-35.png)
> **NV RAM 数据处理**
> 某些情况下需要对nvram的数据进行一定的处理（比如实现自己的crc）
> 通过callback进行处理
> ![alt text](image-36.png)
> 对csm job结果的处理
> ![alt text](image-37.png)
> **写保护**
> 不能再进行写
> write block once 是允许写一次
> ![alt text](image-38.png)
> read all 对写保护的影响
> 注意这两个数据的选项
> ![alt text](image-39.png)
> **block id check**
> crc还会计算block id
> ![alt text](image-40.png)
> **block length check**
> 有永久的ram和永久的rom
> 会在编译阶段check length
> ![alt text](image-41.png)