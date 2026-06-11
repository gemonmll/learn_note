## filters 滤波 下采样

### 基础理论
> 采样原因
> ![Alt text](image.png)
> 采样方法
> 激光雷达采集的为无序点云，深度相机采集的一般为有序点云。
> ![Alt text](image-1.png)
> 一些官方教程
> ![Alt text](image-2.png)
> 直通滤波器 （范围滤波）
> ![Alt text](image-3.png)
> ![Alt text](image-4.png)
> ![Alt text](image-5.png)
> 体素栅格下采样 voxelgrid
> 减少点的数量，同时保留点云形状
> ![Alt text](image-6.png)
> ![Alt text](image-7.png)
> ![Alt text](image-8.png)
> statisticalOutlierRemoval滤波器移除离群点
> ![Alt text](image-9.png)
> ![Alt text](image-10.png)
> 参数化模型投影点云
> ![Alt text](image-11.png)
> ![Alt text](image-12.png)
> 从点云中提取索引
> ![Alt text](image-13.png)
> ![Alt text](image-14.png)
> 使用ConditionalRemoval或RadiusOutlinerRemoval移除离群点
> ![Alt text](image-15.png)
> ![Alt text](image-16.png)
> 双边滤波算法
> ![Alt text](image-17.png)
> 均匀取样
> ![Alt text](image-18.png)