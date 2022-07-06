# 神经网络
import matplotlib.pyplot as plt
import numpy as np

# sigmoid函数
# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))


#
#
# x = np.arange(-5.0, 5.0, 0.1)
# y = sigmoid(x)
# plt.plot(x, y)
# plt.ylim(-0.1, 1.1)
# plt.show()


# x = np.array([1, 2])
# print(x, x.shape)
# w = np.array([[1, 3, 5], [2, 4, 6]])
# print(w, w.shape)
# y = np.dot(x, w)
# print(y, y.shape)

# 三层神经网络的实现
# # 输出层的激活函数
# def identity_function(x):
#     return x
#
#
# # 权重和偏置的初始化 保存在字典变量network中
# def init_network():
#     network = {}
#     network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
#     network['b1'] = np.array([0.1, 0.2, 0.3])
#     network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
#     network['b2'] = np.array([0.1, 0.2])
#     network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
#     network['b3'] = np.array([0.1, 0.2])
#     return network
#
#
# # 封装了将输入信号转换为输出信号的处理过程
# def forward(network, x):
#     W1, W2, W3 = network['W1'], network['W2'], network['W3']
#     b1, b2, b3 = network['b1'], network['b2'], network['b3']
#     a1 = np.dot(x, W1) + b1
#     z1 = sigmoid(a1)
#     a2 = np.dot(z1, W2) + b2
#     z2 = sigmoid(a2)
#     a3 = np.dot(z2, W3) + b3
#     y = identity_function(a3)
#     return y
#
#
# network = init_network()
# x = np.array([1.0, 0.5])
# y = forward(network, x)
# print(y)  # [ 0.31682708 0.69627909]

# # 梯度的实现
# def function_2(x):
#     return np.sum(x ** 2)
#
#
# 数值微分计算梯度法
# def numerical_gradient(f, x):
#     h = 1e-4
#     # 生成一个和x形状相同的数组
#     grad = np.zeros_like(x)
#
#     for idx in range(x.size):
#         tmp_val = x[idx]
#         x[idx] = tmp_val + h
#         fxh1 = f(x)
#         x[idx] = tmp_val - h
#         fxh2 = f(x)
#         grad[idx] = (fxh1 - fxh2) / (2 * h)
#         # 还原值
#         x[idx] = tmp_val
#
#     return grad
# #
# #
# # if __name__ == "__main__":
# #     result = numerical_gradient(function_2, np.array([3.0, 4.0]))
# #     print(result)
#
#
# # 梯度下降法的实现
# def gradient_descent(f, init_x, lr=0.01, step_num=100):
#     x = init_x
#     for i in range(step_num):
#         grad = numerical_gradient(f, x)
#         x -= lr * grad
#
#     return x
#
#
# if __name__ == "__main__":
#     init_x = np.array([-3.0, 4.0])
#     result = gradient_descent(f=function_2, init_x=init_x, lr=0.1, step_num=100)
#     print(result)




