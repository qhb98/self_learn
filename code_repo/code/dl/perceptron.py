# 感知机
import numpy as np


# 感知机的简单实现
# def and_and(x1, x2):
#     w1, w2, theta = 0.5, 0.5, 0.7
#     tmp = x1 * w1 + x2 * w2
#     if tmp <= theta:
#         return 0
#     else:
#         return 1
#
#
# if __name__ == "__main__":
#     result = and_and(0.5, 0.3)
#     print(result)

# 导入权重和偏置
def and_and(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


if __name__ == "__main__":
    result = and_and(0.5, 0.3)
    print(result)
