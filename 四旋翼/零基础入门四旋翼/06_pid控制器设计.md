## **01 pid控制器原理讲解**
> pid原理
> ![Alt text](image-50.png)
> ![Alt text](image-51.png)
> ![Alt text](image-52.png)
## **02 角速度环pid控制器**
> 角速度控制器原理
> ![Alt text](image-53.png)
> 控制过程
> ![Alt text](image-54.png)
> 动力分配 （相当于对原方程求逆运算）
> f是升力， taoxyz是xyz轴力矩
> ![Alt text](image-55.png)
> 姿态环
> ![Alt text](image-56.png)
> 速度环
> ![Alt text](image-57.png)
> 位置环
> ![Alt text](image-58.png)
## **03 代码实现**
> 姿态pid
> ![Alt text](image-59.png)
> 位置pid
> ![Alt text](image-60.png)
## **04 轨迹跟踪控制器**
> 无人机反馈控制
> ![Alt text](image-61.png)
> 反馈+前馈控制 
> 提高响应速度
> ![Alt text](image-62.png)
> 五次样条曲线轨迹控制
> ![Alt text](image-63.png)
> ![Alt text](image-64.png)