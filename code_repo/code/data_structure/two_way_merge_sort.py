# 归并排序
"""
1.把长度为n的输入序列分成两个长度为n/2的子序列
2.对这两个子序列分别采用归并排序
3.将两个排序好的子序列合并成一个最终的排序序列

"""


def merge_sort(lst):
    # 合并左右子序列函数
    def merge(arr, left, mid, right):
        temp = []  # 中间数组
        i = left  # 左段子序列起始
        j = mid + 1  # 右段子序列起始
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= right:
            temp.append(arr[j])
            j += 1
        for i in range(left, right + 1):  # !注意这里，不能直接arr=temp,他俩大小都不一定一样
            arr[i] = temp[i - left]

    # 递归调用归并排序
    def m_sort(arr, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        m_sort(arr, left, mid)
        m_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

    n = len(lst)
    if n <= 1:
        return lst
    m_sort(lst, 0, n - 1)
    return lst


x = input("请输入待排序的数：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = merge_sort(arr)
print("排序结构如下:")
for i in arr:
    print(i, end=' ')
