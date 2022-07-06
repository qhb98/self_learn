# 选择排序
"""
1.初始状态：无序区为R，有序区为空；
2，第i趟排序开始时，当前有序区和无序区分别为R[1,i-1]和R[i,n]。该趟排序从当前无序区中选出关键字最小的记录R[k]，将它与无序区的第1个记录R交换，使R[1,i-1]和R[i,n]分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区。
3.n-1趟结束，数组有序化了。

"""


def select_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            (lst[min_index], lst[i]) = (lst[i], lst[min_index])
    return lst


x = input("请输入待排序的数:")
y = x.split()
arr = []
for i in y:
    arr.append(i)
arr = select_sort(arr)
print("排序结果如下:")
for i in arr:
    print(i, end=" ")
