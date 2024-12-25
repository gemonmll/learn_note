## detr
### 01 DETR 目标检测
> ![alt text](image.png)
> 基本思想
> 套用transformer
> 重点在于decoder
> ![alt text](image-1.png)
### 02 整体网络框架分析
> 解码器并行预测100个坐标框
> ![alt text](image-2.png) 
> 整体网络架构
> ![alt text](image-3.png)
> object queries是核心
> 解码器提供q 编码器提供k v
> ![alt text](image-4.png)
### 03 位置信息初始化query 向量
> encoder完成的任务
> ![alt text](image-5.png)
> 整体网络架构
> object queries 0+位置编码初始化
> ![alt text](image-6.png)
### 04 注意力机制的作用方法
> 有自注意力机制和注意力机制  
> 最后连上两个全连接一个分类一个回归任务
> ![alt text](image-7.png)
### 05 训练过程的策略
> 输出的匹配
> ![alt text](image-8.png)
> 小的细节
> ![alt text](image-9.png)

### detr 源码实现
> 