# import torch
#
# # 创建一个张量，设置requires_grad=True来跟踪与它相关的计算
# x = torch.ones(2, 2, requires_grad=True)
# print(x)
#
# # 针对一个张量操作
# y = x + 2
# print(y)
# print(y.grad_fn)
#
# # 针对y做更多的操作
# z = y * y * 3
# out = z.mean()
# print(z, out)
# # .requires_grad()会改变张量的requires_grad标记，输入的标记默认为False
#
# a = torch.randn(2, 2)
# a = ((a*3) / (a-1))
# print(a.requires_grad)
# a.requires_grad_(True)
# print(a.requires_grad)
# b = (a * a).sum()
# print(b.grad_fn)


# 定义神经网络
import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        # 1 input image channel, 6 output channels, 5*5 square convolution

        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)







