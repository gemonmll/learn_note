## chapter5 仿真
### 目录
> ![Alt text](image.png)

### 5.1 仿真的必要性及常见仿真工具介绍
> 仿真的意义
> ![Alt text](image-1.png)
> ![Alt text](image-2.png)

### 5.2 仿真模块介绍及源码分析
> 模块介绍
> ![Alt text](image-3.png)
> 代码分析及实践
> mini_sil_env
> ![Alt text](image-4.png)
> ![Alt text](image-5.png)
> 车辆模型
> ![Alt text](image-6.png)
> world模型
> ![Alt text](image-7.png)
> 解析车辆模型的插件
> ![Alt text](image-8.png)
> 车辆动力输入的插件
> ![Alt text](image-9.png)
> 车辆控制的输入 底盘控制
> ![Alt text](image-10.png)
> tf坐标变换
> ![Alt text](image-11.png)
> 读取车辆基本信息 订阅 发布
> 与gazebo交互桥梁
> ![Alt text](image-12.png)
> #### 切换仿真环境 
> ![Alt text](image-13.png)
> world文件解析
> 加载了个插件
> ![Alt text](image-14.png)
> ![Alt text](image-15.png)
> ![Alt text](image-16.png)
> 车辆urdf文件解析
> urdf 传感器插件
> ![Alt text](image-18.png)
> 车辆基本参数
> ![Alt text](image-19.png)
> ![Alt text](image-20.png)
> ![Alt text](image-21.png)
> 传感器配置
> ![Alt text](image-22.png)
> ![Alt text](image-23.png)

### 5.3 实践：车辆加入传感器
> ![Alt text](image-24.png)
> ![Alt text](image-25.png)
> ![Alt text](image-26.png)

### 5.4 仿真环境下的感知与定位
> ![Alt text](image-27.png)
> 有和gazebo通信的bridge需要启动
> ![Alt text](image-28.png)
> ![Alt text](image-29.png)

### 5.5 作业讲解
> ![Alt text](image-30.png)
> ![Alt text](image-31.png)
> ![Alt text](image-32.png)
> ![Alt text](image-33.png)