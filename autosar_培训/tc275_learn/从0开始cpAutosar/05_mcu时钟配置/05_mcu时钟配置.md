## 05 mcu时钟配置
> ### 5.1 概述
> 主要内容：时钟源，倍频，时钟分配
> ![alt text](image.png)
> 时钟分布图
> ![alt text](image-1.png)
> ### 5.2 时钟生成
> 时钟源一般有两个（外部晶振，内部backup）
> ![alt text](image-2.png)
> ### 5.3 时钟倍频
> 由系统pll和外设pll构成
> 20M倍频到300M
> ![alt text](image-3.png)
> 系统pll为例子，计算公式
> fpll0 由 N P K2计算得到
> ![alt text](image-4.png)
> 系统pll和外设pll异同点
> ![alt text](image-5.png)
> ### 5.4 时钟分配
> 主要关注两点（时钟源是哪个，如何倍频）
> ![alt text](image-6.png)
> 外部时钟输入
> 通过引脚提供两个外部时钟
> ![alt text](image-7.png)
> clock monitoring 时钟监控
> ![alt text](image-8.png)
> ### 5.5 Mcan时钟分频过程
> ![alt text](image-9.png)
> ### 5.6 STM时钟分配
> 300M输入，1/3分配 得到100M时钟
> ![alt text](image-10.png)
> ### 5.7 davinci配置
> 系统时钟配置
> ![alt text](image-11.png)
> 时钟分配
> ![alt text](image-12.png)
> mcan配置 时钟选择
> ![alt text](image-13.png)
> stm时钟配置
> ![alt text](image-14.png)
> 系统pll的配置
> ![alt text](image-15.png)
> 外设pll的配置，多了k3的配置
> ![alt text](image-16.png)
> ### 5.8修复时钟不准bug
> 修改vbrs中的system timer配置,配置成计算的100M（只是宏观参考，不会对板子有影响）
> ![alt text](image-17.png)
> 计数器对应更改
> ![alt text](image-18.png)