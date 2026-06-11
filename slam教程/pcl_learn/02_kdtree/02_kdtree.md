## kdtree
> 一种分割K维数据空间的数据结构，用于多维空间关键数据的搜索（范围搜索和最近邻搜索）。
> ![Alt text](image.png)
> 例子如下
> kd树算法要确定分割线
> ![Alt text](image-1.png)
> kd树算法分为两个部分，一部分是有关k-d树本身这种数据结构建立的算法，另一部分在建立的kd树上进行最近邻查找。
> kd树算法（构造）
> ![Alt text](image-2.png)
> kd树上的knn算法（搜索）
> ![Alt text](image-3.png)
> 点云上的搜索
> ![Alt text](image-4.png)
> pcl kdtree flann（快速最近邻搜索包）
> ![Alt text](image-5.png)
>
## kdtree代码部分
![Alt text](image-11.png)
> 创建点云
> ![Alt text](image-6.png)
> 创建kdtree对象，并设置搜索点
> ![Alt text](image-7.png)
> k近邻搜索
> ![Alt text](image-8.png)
> ![Alt text](image-9.png)
> 结果
> ![Alt text](image-10.png)
> 半径搜索
> ![Alt text](image-12.png)