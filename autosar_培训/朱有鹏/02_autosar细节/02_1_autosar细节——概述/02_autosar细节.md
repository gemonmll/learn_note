## 2.1 autosar 细节学习资源
> 学习资源
> 官网很重要，重点是starndards下的几种autosar标准
> 两篇博客
> ![alt text](image.png)
## 2.2 AutosarCp分层和分模块解读
> Autosar标准起的名字和概念
> 三个粒度分层：App\RTE\BSW
> ![alt text](image-1.png)
> ![alt text](image-3.png)
> detail view
> ![alt text](image-2.png)
> BSW分为三层4部分：service层、ECU抽象层、MCAL微控制器抽象层
> ![alt text](image-4.png)
> ![alt text](image-5.png)
> BSW纵向分模块

## 2.3 autosarCP各软件分层解读
> ### BSW各模块分层
> ![alt text](image-12.png)
> 2.4.1 MCAL
> 内部驱动（外部驱动在ECU层） MCU级别抽象、芯片无关
> ![alt text](image-6.png) 
> ECU 抽象层 （外部设备驱动） 板卡级别抽象、真正的硬件无关
> ![alt text](image-7.png)
> CDD 复杂驱动（非标准设备）
> ![alt text](image-8.png)
> services layer 服务层（逻辑层面 OS 程序流监控 与APP存在相关性），IO的服务层和ECU抽象层放在一起
> TASK 提供APPL基本服务支持、RTE、bsw
> 实现，大部分mcu ecu无关,有一部分os相关
> ![alt text](image-9.png)
> RTE层 runtime env运行时环境 （汽车是一个大的网络，对各个节点抽象，操作可能会跨ECU (RTE会区分两个SWC是否在一个ECU内部)）
> 提供通信服务（app和sensor传感器\actuator执行器） APPL可以不考虑是否要跨ECU,RTE去处理
> 上层不再分层，只会分components(swc),多个SWC通信依赖RTE、对下依赖RTE
>##### 任务：让swc无关具体的ECU
> 实现： 与ECU和APP相关 对上： 与ECU无关
> ![alt text](image-11.png)

## 2.4 autosar cp 软件层的几个概念
>  ![alt text](image-13.png)
> types of services 
> memory(flash store类型的，非sram的)
> crypto 加密
> system(os error timer) ECU specific(ecu 状态，watchdog)
> ![alt text](image-14.png)
> internal driver 位于MCAL
> ![alt text](image-15.png)
> EXternal driver 位于ECU
> ![alt text](image-16.png)
> interface :通常在ECU抽象层，提供标准API
> ![alt text](image-17.png)
> handler 特定的interface ,异步访问driver
> 不处理具体数据
> 通常是集成在了driver和interface中（SPIHandlerDriver,ADCDriver）
> ![alt text](image-18.png)
> manager 给多个clients 提供服务，位于services layer
> 在handler搞不定的情况下，使用mananger
> 还可以去评估 更改 适配
> 示例 NVRAM manager 管理 内部，外部 flash 访问，提供 data storage\data checking
> ![alt text](image-19.png)
> ##### driver(寄存器操作)、handler和manager 提供异步操作，仲裁，三个概念构成全部的硬件操作
> library 公共库 （同步 可重入 不需要初始化）
> ![alt text](image-20.png)

## 2.5 BSW的软件模块和开源代码
> ![alt text](image-22.png)
> driver
> ![alt text](image-21.png)
> kernel (适配rtos)
> ![alt text](image-23.png)
> boards (ecu 设计、模型文件生成的配置文件)
> ![alt text](image-24.png)
> ![alt text](image-25.png)
> c 库、 common
> ![alt text](image-26.png)
> ![alt text](image-27.png)
> comm、diag(dcm dem det)
> drivers(mcal驱动 ecu驱动)
> examples(os、RTE)
> mem(memory EA FEE )
> system(system service (os kernel\ ecum\iohdware schm mm wdgm  ))
> #### ecu层级并不是一一对应的，mcal层级一一对应
> ![alt text](image-29.png)
> ![alt text](image-28.png)
> 