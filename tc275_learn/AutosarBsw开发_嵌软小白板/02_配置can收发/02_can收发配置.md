##  应用报文开发
> ### 1 认识can矩阵 dbc
> ![alt text](image.png)
> ![alt text](image-2.png)
> 通过dbc可以配置报文属性（网管报文，等等）方便应用软件配置，一般来说直接导入属性
> ![alt text](image-3.png)
> ![alt text](image-4.png)
> ![alt text](image-5.png)
> messaage 属性
> 周期 ，应用报文
> ![alt text](image-6.png)
> 发送方
> ![alt text](image-7.png)
> ![alt text](image-8.png)
> ### 2 应用报文变更开发
> ![alt text](image-9.png)
> ![alt text](image-10.png)
> ![alt text](image-11.png)
> ![alt text](image-12.png)
> **删除一条应用报文，新增一个can信号，删除一个can信号**
> **需求如下**
> ![alt text](image-14.png)
> **修改dbc**
> 删除报文一般在msg中直接干掉
> ![alt text](image-15.png)
> 改变信号大小
> ![alt text](image-16.png)
> 变更周期
> ![alt text](image-17.png)
> **修改bsw文件**
> update之前更新developer位置
> ![alt text](image-19.png)
> update dbc
> 第一个选项
> ![alt text](image-18.png)
> ![alt text](image-20.png)
> 0x115报文已经没了
> ![alt text](image-21.png)
> dbc要拖到signal group中
> 每次生成完代码要比对小差异，很重要
> ![alt text](image-22.png)
> 为了防止asw中有信号，bsw虽然删除了，但也会生成空的接口
> ![alt text](image-23.png)
> **需要在asw层删除掉连线**
> 删除0x115object
> ![alt text](image-24.png)
> ![alt text](image-25.png)
> 存在错误 0x114修改起始位置后不匹配
> ![alt text](image-27.png)
> ![alt text](image-26.png)
> 需要与bsw 同步下 adapt后重新map
> ![alt text](image-28.png)
> ![alt text](image-29.png)
> ![alt text](image-30.png)
> 删除其他的 object 重新maP
> ![alt text](image-31.png)
> create port\重新接线
> ![alt text](image-32.png)
> ![alt text](image-33.png)
> 真正在模块中调用write接口 read 接口
> ![alt text](image-34.png)
> ![alt text](image-35.png)
> **在beyond compare中比对下差异**
> ![alt text](image-36.png)
> 编译中把app的文件删除掉
> ![alt text](image-37.png)
> ### 课时3 每条接收报文配置邮箱