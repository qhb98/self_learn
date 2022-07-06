# convolutional neural network

# CNN中新增了Convolution层和Pooling层，连接顺序是“Convolution-ReLU-Pooling”。但是在最靠近输出的层中使用了Affine-ReLU的组合，最后的输出层则是Affine-Softmax组合。
# CNN各层间传递的数据都是4维数据

# 全连接层 fully connected layers 综合前边提取到的所有特征
# 全连接层的参数很多，对模型影响主要有：全连接层的总层数(长度)，单个全连接层的神经元数(宽度)，激活函数(增加模型的非线性表达能力)
# 全连接层存在的问题是：会忽略数据的形状，无论输入是几维数据，都会被拉平到1维数据

# 卷积层 Convolution 可以保持数据的形状不变  卷积运算就相当于滤波器运算(对于输入数据，卷积运算以一定间隔滑动滤波器的窗口并应用)
# 填充 padding 幅度为1的填充==用幅度为1像素的0填充周围
# 步幅 stride  应用滤波器的位置间隔

# 输入大小为(H, W) 滤波器大小为(FH, FW) 输出大小为 (OH, OW) 填充为P 步幅为S
# 则卷积运算的公式为
# OH=(H+2P-FH)/S+1  OW=(W+2P-FW)/S+1

# 三维数据(channel, height, width)的卷积运算：当通道上有多个特征图时，会按通道进行输入数据和滤波器的卷积运算，并将结果相加，从而得到输出。

# 池化层 pooling 池化是缩小高、长方向上的空间的运算
# 池化层没有要学习的参数，只是从目标区域中取出最大值或平均值；且 通道数不发生变化，计算是按通道独立进行的；对微小的位置变化具有鲁棒性

import numpy as np
# 随机生成10个 通道数为1，高为28，长为28的数据
x = np.random.rand(10, 1, 28, 28)
# print(x, x.shape, x.size)

# 网络结构
# LeNet  使用的激活函数是sigmoid函数，使用子采样subsampling缩小中间数据的大小
# AlexNet  激活函数使用ReLU 使用进行局部正规化的LRN层local response normalization  使用Dropout



