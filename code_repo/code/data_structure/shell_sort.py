# 希尔排序
"""
1.选择一个增量序列t1,t2,...,tk，其中ti>tj，tk=1
2.按增量序列个数k，对序列进行k躺排序
3.每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m的子序列，分别对各子表进行直接插入排序。仅增量因子为1时，整个序列作为一个表达来处理，表长度即为整个序列的长度。

"""


def shell_sort(lst):
    def shell_insert(arr, d):
        n = len(arr)
        for i in range(d, n):
            j = i - d
            temp = arr[i]
            # 记录要出入的数
            while j >= 0 and arr[j] > temp:
                # 从后向前，找更小的数的位置
                arr[j + d] = arr[j]
                # 向后移动
                j -= d
            if j != i - d:
                arr[j + d] = temp

    n = len(lst)
    if n <= 1:
        return lst
    d = n // 2
    while d >= 1:
        shell_insert(lst, d)
        d = d // 2
    return lst


x = input("请输入待排序的数:")
y = x.split()
arr = []
for i in y:
    arr.append(i)
arr = shell_sort(arr)
print("排序结果如下:")
for i in arr:
    print(i, end=" ")
