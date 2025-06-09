## 基于图优化的slam方法
> 基于滤波器的方法（只是估计当前状态）,只是估计xt
> 基于图优化的方法 (可以优化之前状态),可以估计x0-xt

### 课程内容
> ![Alt text](image.png)

### graph-based slam
> 图优化概念
> ![Alt text](image-1.png)


### 非线性最小二乘
> 解决问题
> ![Alt text](image-2.png)
> ![Alt text](image-3.png)
> 带有权重的误差 观测值的可靠性
> 加权最小二乘
> ![Alt text](image-4.png)
> 解决的问题
> ![Alt text](image-5.png)
> 线性化的过程
> ![Alt text](image-6.png)
> ![Alt text](image-8.png)
> ![Alt text](image-9.png)
> 求解
> ![Alt text](image-10.png)
> 流程
> ![Alt text](image-11.png)

### 非线性最小二乘在slam中的应用
> 图的构建
> ![Alt text](image-12.png)
> 误差定义
> ![Alt text](image-13.png)
> 误差函数
> ![Alt text](image-14.png)
> 误差函数线性化
> ![Alt text](image-15.png)
> 稀疏向量
> ![Alt text](image-16.png)
> ![Alt text](image-17.png)
> 固定坐标系 选择第一个位姿为0
> 额外的约束
> ![Alt text](image-18.png)
> ![Alt text](image-20.png)
> 构建线性系统
> ![Alt text](image-21.png)
> ![Alt text](image-22.png)

### cartographer 
> ![Alt text](image-23.png)