## TC275 架构
> ### 1 概述
> 整体架构
> ![alt text](image.png)
> 安全相关
> ![alt text](image-1.png)
> 参考资料
> ![alt text](image-2.png)
> ![alt text](image-3.png)
> ### 2 TC1.6E/1.6P 内核结构
> 内核发展
> ![alt text](image-4.png)
> 内核主要结构
> ![alt text](image-5.png)
> TC275内核
> 共享资源互联 SRI
> ![alt text](image-6.png)
> 单核与多核之间的对比
> ![alt text](image-7.png)
> SRI总线特点
> ![alt text](image-8.png)
> ![alt text](image-9.png)
> 主要的主机是行， 主要从机为列
> ![alt text](image-10.png)
> 内核子系统
> ![alt text](image-11.png)
> 四级流水线和六级流水线
> ![alt text](image-12.png)
> ![alt text](image-13.png)
> ![alt text](image-14.png)
> ![alt text](image-15.png)
> 主要寄存器
> 16个地址寄存器和16个数据寄存器
> 还有程序状态字 PC等寄存器
> ![alt text](image-17.png)
> 各个寄存器 低级高级上下文
> ![alt text](image-18.png)
> 其他寄存器
> ![alt text](image-19.png)
> 程序状态字
> ![alt text](image-20.png)
> #### 3 上下文保护
> 上下文分为高级上下文和低级上下文
> 高级上下文是针对任务的，包含当前上下文信息PCXI和程序状态字
> 低级上下文针对参数传递
> ![alt text](image-21.png)
> ![alt text](image-22.png)
> ![alt text](image-23.png)
> 高级低级分类，不同的保护保存在不同的izhi
> ![alt text](image-24.png)
> 上下文保护Areas
> 端地址和16位偏移 用来产生链接地址 linked CSA
> 64Bytes边界
> ![alt text](image-25.png)
> ![alt text](image-26.png)
> 链接字的产生
> ![alt text](image-27.png)
> 上下文的保护过程
> ![alt text](image-28.png)
> ![alt text](image-29.png)
> 上下文的恢复
> ![alt text](image-30.png)
> ![alt text](image-31.png)
> #### 4 保护系统
> ![alt text](image-32.png)
> 保护系统目标
> 防止内核受到软件错误的影响
> 避免多个app访问同一资源冲突
> 提供测试和调试功能 
> 主要机制：陷阱系统、访问权限、存储器保护系统
> ![alt text](image-33.png)
> ![alt text](image-34.png)
> 三种mode
> ![alt text](image-35.png)
> user-0
> ![alt text](image-36.png)
> user-1
> ![alt text](image-37.png)
> Supervisor
> ![alt text](image-38.png)
> 存储器保护 四个set
> ![alt text](image-39.png)
> ![alt text](image-40.png)
> ![alt text](image-41.png)
> 代码保护执行使能
> ![alt text](image-42.png)
> ![alt text](image-43.png)
> 代码保护范围寄存器
> ![alt text](image-44.png)
> 存储器保护案例
> ![alt text](image-45.png)
> ![alt text](image-46.png)
> 案例2
> ![alt text](image-47.png)
> ![alt text](image-48.png)
> ![alt text](image-49.png)
> ![alt text](image-50.png)
> ![alt text](image-51.png)
> 临时保护系统
> 用于保护系统避免超时运行
> ![alt text](image-52.png)
> ![alt text](image-53.png)
> #### 5 存储器 （PMI DMI SRAM Cache PMU Flash）
> 所有存储器分为16个区，每个区256M
> 扇区0-7 用于cpu 程序快速访问SRAM
> 扇区8 用于缓存扇区 包含pflash boot rom ebu的访问
> 扇区9 LMU SRAM EMEM
> 扇区10  PFLASH DFLASH BOOTROM
> 扇区15 寄存器
> ![alt text](image-54.png)
> 支持8个多核处理器 扇区0-7
> 每个核都有自己全局的扇区
> 每个核都可以访问扇区C核扇区D
> ![alt text](image-56.png)
> 局部存储器
> ![alt text](image-57.png)
> LMU
> ![alt text](image-58.png)
> FLASH
> ![alt text](image-59.png)
> PMI和DMI 概述
> ![alt text](image-60.png)
> PMI 两种联动的缓存方式 受到ECC保护
> PSPR 通过SRI接口享有全局资源
> ![alt text](image-61.png)
> ![alt text](image-62.png)
> ![alt text](image-63.png)
> ![alt text](image-64.png)
> DMI 数据存储接口
> ![alt text](image-65.png)
> ![alt text](image-66.png)
> ![alt text](image-67.png)
> PMU 通过XBAR_SRI总线访问PFLASH
> ![alt text](image-68.png)
> ![alt text](image-69.png)
> ![alt text](image-70.png)
> PF0
> ![alt text](image-71.png)
> Aurix EEPROM
> ![alt text](image-72.png)
> #### 6 复位系统与启动系统
> 四种复位 复位系统
> ![alt text](image-73.png)
> 三个引脚
> ![alt text](image-74.png)
> 复位类型
> ![alt text](image-75.png)
> 复位引脚
> ![alt text](image-76.png)
> 复位过程
> ![alt text](image-77.png)
> 启动系统
> ![alt text](image-78.png)
> ![alt text](image-79.png)
> ![alt text](image-80.png)
> BMI启动校验头
> ![alt text](image-81.png)
> ![alt text](image-82.png)
> ![alt text](image-83.png)
> 启动引导程序
> ![alt text](image-84.png)
> ![alt text](image-85.png)
> ![alt text](image-86.png)
> #### 7 中断系统
> 中断系统框图
> 五个独立的中断服务提供者 3个cpu 1个DMA 1个SDMA
> ICU 中断控制单元
> SRN+Arbitration Bus+ICU 称为Interrupt Router
> ![alt text](image-87.png)
> ![alt text](image-88.png)
> ![alt text](image-89.png)
> 处理中断请求的是服务提供者
> ![alt text](image-90.png)
> 中断路由器
> ![alt text](image-91.png)
> ![alt text](image-92.png)
> 各个寄存器
> ![alt text](image-93.png)
> ![alt text](image-94.png)
> ![alt text](image-95.png)
> ![alt text](image-96.png)
> 仲裁系统
> ![alt text](image-97.png)
> 使用例程
> ![alt text](image-98.png)
> ![alt text](image-99.png)
> #### 8 时钟系统
> ![alt text](image-100.png)
> 概述
> ![alt text](image-101.png)
> 支持独立的时钟
> ![alt text](image-102.png)
> ![alt text](image-103.png)
> ![alt text](image-104.png)
> ![alt text](image-105.png)
> 三种模式
> ![alt text](image-106.png)
> ![alt text](image-107.png)
> prescaler mode b不稳定
> ![alt text](image-108.png)
> ![alt text](image-109.png)
> free running
> ![alt text](image-110.png)
> ![alt text](image-111.png)
> 时钟输出
> ![alt text](image-112.png)
> 时钟源选择
> ![alt text](image-113.png)
> ![alt text](image-114.png)
> 示例
> ![alt text](image-115.png)
> ![alt text](image-116.png)
> 时钟监控
> 利用备用100mHZ监控
> ![alt text](image-117.png)
> #### 9 供电系统
> 概述
> ![alt text](image-118.png)
> ![alt text](image-119.png)
> ![alt text](image-120.png)
> ![alt text](image-121.png)
> ![alt text](image-122.png)
> 电源管理
> ![alt text](image-123.png)