from __future__ import print_function
import torch


# 构建一个5*3的矩阵，不初始化
a = torch.empty(5, 3, dtype=torch.int)
print(a)

# 构造一个随机初始化的矩阵
b = torch.rand(5, 3)
print(b)

# 构造一个矩阵全为0，而且数据类型是long
c = torch.zeros(5, 3, dtype=torch.long)
print(c)

# 构造一个张量，直接使用数据
d = torch.tensor([5.5, 3])
print(d)

# 基于已存在的tensor创建一个新的tensor
e = torch.ones(4, 3, dtype=torch.float)
print(e)
f = torch.randn_like(e, dtype=torch.double)
print(f)

# 获取维度信息
print(f.size())

# 张量相加操作
g = torch.add(a, b)
print(g)

# 任何使张量会发生变化的操作都有一个前缀 x.copy(y),x.t_()或者使用numpy类似的索引操作
print(g[:, 1])

# 改变张量的大小
x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)
print(x, x.size(), y, y.size(), z, z.size())






