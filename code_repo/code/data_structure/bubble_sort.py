# 冒泡排序
"""
· 1.比较相邻的元素。如果第一个比第二个大，就交换它们两个；
· 2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
· 3.针对所有的元素重复以上的步骤，除了最后一个；
· 4.重复步骤1~3，直到排序完成。

"""


def BubbleSort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(0, n):
        # i 是用来标记正在进行排序的数所处的位置的
        for j in range(0, n - i - 1):
            # j 用来从lst中取出两两相邻的数
            if lst[j] > lst[j + 1]:
                (lst[j], lst[j + 1]) = (lst[j + 1], lst[j])
    return lst


# 整理输入的数据格式为列表
x = input("请输入待排序的数: ")
# 输入待排序的数列
y = x.split()
# 切片 以空格为分隔符进行分割 返回分割后的列表
arr = []
for i in y:
    arr.append(int(i))
arr = BubbleSort(arr)
print("排序结果如下:\n")
for i in arr:
    print(i, end=" ")
