## transformer解读
### 01 BERT 网络模型
> 自然语言处理通用解决方案
> 重点在transformer网络架构
> ![alt text](image.png)
### 02 传统解决方案遇到的问题
> 基本任务 seq2seq网络
> ![alt text](image-1.png)
> 传统的RNN网络 无法并行任务
> ![alt text](image-2.png)
> transformer 可以同时计算，同时有attention机制
> ![alt text](image-3.png)
> 传统的word2vec
> ![alt text](image-4.png)
> transformer整体结构
> ![alt text](image-5.png)
### 03 注意力机制的作用
> attention啥意思
> ![alt text](image-6.png)
> 根据不同的数据找到不同的注意点
> it 这个词 是受the annimal 影响最大
> ![alt text](image-7.png)
### 04 self attention 计算方法
> self attention 计算方法 构建q k v矩阵
> ![alt text](image-8.png)
> q k v矩阵 三个需要训练的矩阵
> 要去查询的 等着被查的 实际的特征信息
> ![alt text](image-9.png)
> 计算方法 q k 内积表示多匹配 相关程度
> ![alt text](image-10.png)
### 05 特征分配与softmax机制
> self attention 计算方法
> 每一个词都要去算 除以dk,则是避免由于向量维度越大越重要
> ![alt text](image-11.png)
> 每一个词的attention计算 qk计算得分，基于得分分配特征
> ![alt text](image-12.png)
> 整体计算流程如下：
> ![alt text](image-13.png)
### 06 Multi-head的作用
> multi-headed机制 多组qkv表示特征表达 类似卷积核
> ![alt text](image-14.png)
> 通过不同的head 得到多个特征表达
> ![alt text](image-15.png)
> ![alt text](image-17.png)
> multi-headed结果
> 不同的注意力结果，得到的特征向量表达也不相同
> ![alt text](image-18.png)
> 堆叠多层
>  ![alt text](image-20.png)
### 07 位置编码与多层堆叠
> 位置信息表达 
> self attention 每个词都会考虑整个序列加权，会出现位置并不会对结果产生影响的问题
>  加入位置信息编码，对于每一个词处理考虑位置
> 还需要加上位置的信息编码
> ![alt text](image-21.png)
> 残差连接与归一化
> layer normalize
> ![alt text](image-22.png)
### 08 transformer 整体架构梳理
> decoder端
> attention 计算不同
> encoder提供k v decoder提供q
> 多了mask机制 因为结果不能一口气都出来
> ![alt text](image-23.png)
> 最终输出结果
> ![alt text](image-24.png)
> 整体梳理
> ![alt text](image-25.png)
> ![alt text](image-26.png)
### 09 BERT 模型训练方法
> ![alt text](image-27.png)
> BERT 就是transformer中的encoder部分
> ![alt text](image-28.png)
> 训练BERT方法
> 1 随机mask方法
> ![alt text](image-29.png)
> 2 预测两个句子是否该连在一起
> ![alt text](image-30.png)
### 10 训练实例
> 所有任务一起训练
> ![alt text](image-31.png)
> 使用BERT,单独两个向量 start 和 end
> ![alt text](image-32.png)
> ![alt text](image-33.png)