# 插入排序
"""
1.从第一个元素开始，该元素可以认为已经被排序
2.取出下一个元素，在已经排序的元素序列中从后向前扫描
3.如果该元素大于新元素，将该元素移到下一位置
4.重复步骤3，直到找到已排序的元素小于或等于新元素的位置
5.将新元素插入到该位置后
6.重复步骤2~5

"""


def insert_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(1, n):
        j = i
        target = lst[i]
        # 每次循环的一个待插入的数
        while j > 0 and target < lst[j - 1]:
            # 比较、后移，给target腾位置
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = target
        # 把target插到空位
    return lst


x = input("请输入待排序数:")
y = x.split()
arr = []
for i in y:
    arr.append(i)
arr = insert_sort(arr)
print("排序结果如下:")
for i in arr:
    print(i, end=" ")
