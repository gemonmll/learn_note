## 02 application
### autosar之前
各个模块嵌套在一起，对模块化分离都不是很友好
底层标准化
![alt text](image.png)
![alt text](image-1.png)
### autosar
核心标准化 arxml 方法论
![alt text](image-2.png)
### 可复用性
> ![alt text](image-3.png)

### 应用层
> 车灯示例
> ![alt text](image-4.png)
> 通信 virtual function bus 是所有port口和connector的集合
> ![alt text](image-6.png)
> rte 是ecu virtual function bus的代表
> ![alt text](image-7.png)

### swc的类型
> atomic component 原子类型
> 又有两种划分 application sensor/actuator
> ![alt text](image-8.png)
> composition 部分， 把原子类型组合起来
> 逻辑架构 复合类型 不会生成代码
> ![alt text](image-9.png)

### port 类型
> RS CS
![alt text](image-10.png)
> Sender Receiver 类型 主要进行数据的传输
> rte_read_xxx
> ![alt text](image-11.png)
> CS client server类型
> 不是通过swc决定的，通过接口决定
> ![alt text](image-12.png)

### runnables
> 可执行实体 需要实现
> ![alt text](image-13.png)

### 例子
> ![alt text](image-14.png)