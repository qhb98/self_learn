"""
这份.py文件使用minist数据集，演示了如何使用pytorch搭建神经网络、循环和测试的全过程
"""


import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
from torch.utils.data import DataLoader
import torchvision
import torchvision.transforms as transforms
from tqdm import *
import matplotlib.pyplot as plt

# 定义数据集 这里使用MINIST数据集
train_dataset = torchvision.datasets.MNIST(root='../../data',
                                           train=True,
                                           transform=transforms.ToTensor(),
                                           download=True)

test_dataset = torchvision.datasets.MNIST(root='../../data',
                                          train=False,
                                          transform=transforms.ToTensor())

# Data loader
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=100,
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=100,
                                          shuffle=False)


# 创建一个4层全连接神经网络 输入层和第一层隐藏层采用relu激活函数 最后的输出层采用softmax激活函数
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # 创建4层全连接神经网络
        self.fc1 = nn.Linear(28*28, 200)
        self.fc2 = nn.Linear(200, 200)
        self.fc3 = nn.Linear(200, 10)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return F.log_softmax(x)


# 神经网络实例化
net = Net()
print(net)

# 训练网络
# 设置参数
learning_rate = 0.01
epochs = 10
log_interval = 120
# 创建一个随机梯度下降优化器
optimizer = torch.optim.SGD(net.parameters(), lr=learning_rate, momentum=0.9)
# 创建一个损失函数
criterion = nn.NLLLoss()

# 保存训练时的损失函数值
train_loss_hist = []
# 运行主训练循环
for epoch in tqdm(range(epochs)):
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = Variable(data), Variable(target)
        # .view()函数对pytorch变量操作，以改变形状，将数据变成(batch_size,784)的维度
        data = data.view(-1, 28*28)
        # 使模型中的所有梯度归零 方便下一次反向传播
        optimizer.zero_grad()
        # 将输入数据批处理传递到模型
        net_out = net(data)
        # 计算损失值
        loss = criterion(net_out, target)
        # 反向传播
        loss.backward()
        # 随机梯度优化
        optimizer.step()
        if batch_idx % log_interval == 0:
            train_loss_hist.append(loss.data)
            print("Train Epoch:" + str(epoch) + "; " + "Loss:" + str(loss.data))


# 运行测试循环
test_loss = 0
correct = 0
for data, target in test_loader:
    with torch.no_grad():
        data, target = Variable(data), Variable(target)
    data = data.view(-1, 28*28)
    net_out = net(data)
    # 对批处理损失求和
    test_loss += criterion(net_out, target).data
    # 得到有最大log概率的下标
    pred = net_out.data.max(1)[1]
    # 比较两个张量中的值，匹配返回1，否则0
    correct += pred.eq(target.data).sum()

test_loss /= len(test_loader.dataset)
print("Average loss:" + str(test_loss) + "; " + "Accuracy:" + str(100*correct/len(test_loader.dataset)))

# 保存神经网络模型
torch.save(net.state_dict(), './model.pt')
# 加载神经网络模型
model_dict = torch.load("./model.pt")

# 训练过程的损失函数值可视化
plt.figure()
plt.plot(train_loss_hist)
plt.show()


