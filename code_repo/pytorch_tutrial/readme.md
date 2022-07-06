# pytorch入门教程

## 一、learn

### 1.1 张量tensor
#### A 
在深度学习中，tensor实际上就是一个多维数组 multidimensional array，其目的就是创造更高维度的矩阵、向量  

|阶|数学实例|python例子|  
|:----:|:----:|:----:|
|0|纯量 (只有大小)|s = 483|
|1|向量(大小和方向)|v = [1.1, 2.2, 3.2]|
|2|矩阵(数据表)|m = [[1, 2, 3], [1, 2, 3], [3, 4, 5]]|
|3|3阶张量(数据立体)|t = [[[2], [3]], [[4], [3]], [[3], [6]]]|
|n|n阶|...|

#### B
tensor对象有3个属性:  
+ rank: number of dimensions
+ shape: number of rows and columns
+ type: data type of tensor's element


### 1.2 自动微分
#### A
+ autograd包是pytorch中所有神经网络的核心。为tensors上的所有操作提供自动微分。
+ torch.Tensor 是包的核心类，若.requires_grad设置为True，则会开始跟踪针对tensor的所有操作。完成计算后，可以调用.backward()自动计算所有的梯度，那么该张量的梯度将累积到.grad属性中。
+ 

#### B
一个典型的神经网络训练过程包括以下几点：  
1.定义一个包含可训练参数的神经网络  
2.迭代整个输入  
3.通过神经网络处理输入  
4.计算损失loss  
5.反向传播梯度到神经网络的参数  
6.更新网络的参数，典型的用一个简单的更新方法： weight = weight - learning_rate * gradient  
7.运行测试集观察效果  
8.保存模型
9.加载训练完成的模型进一步使用

refer to [https://zhuanlan.zhihu.com/p/398473068](https://zhuanlan.zhihu.com/p/398473068)



#### C 动态计算图 dynamic computational graph
![](F:\PycharmCode\code_repo\pytorch_tutrial\figure\1.2.1.png)

图中是在requires_grad=False的情况下。  
每个虚线框是一个变量variable，每个紫色矩形框是一个操作，每个variable对象都有一些成员。  

+ data: 是一个variable所持有的数据。x持有一个1*1的tensor，值为1.0。
+ requires_grad: 若True，追溯所有的操作记录，建立一个梯度计算的反向传播图。
+ grad: grad持有梯度的值，若requires_grad是False，会持有一个None值，若为True，依旧持有一个None值，除非**.backward()函数在其他节点被调用
+ grad_fn: 用于计算梯度的反向函数 backward function
+ is_leaf: 一个节点是树叶。在调用.backward()时，梯度只填充于那些requires_grad is_leaf都为True的节点。
+ 


![](F:\PycharmCode\code_repo\pytorch_tutrial\figure\1.2.2.png)

图中是在requires_grad=True的情况下。

#### D backward()
+ 反向函数，在反向图中从调用它的根tensor到根tensor可到达的叶子节点中的所有路径通过传递它的参数来计算梯度。  
+ 被计算出来的梯度被存储在每个叶子节点的.grad中。  
+ 反向图在前向传播 forward pass 的过程中已经被动态创建了，反向函数只需要使用已经被创建的图来计算梯度，并将它们存储在叶子节点中。
+ 



