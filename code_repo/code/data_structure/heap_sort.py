# 堆排序
"""
1.将初始排序关键字序列构建成大顶堆，此堆为初始的无序区
2.将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区和新的有序区，且满足R[1,2,...,n-1]<=R[n]
3.重新调整当前无序区的堆的为新堆，再进行交换，得到新的无序区和新的有序区
4.重复步骤1~3

"""


def head_sort(lst):
    def heap_adjust(arr, start, end):
        # 将以start为根节点的堆调整为大顶堆
        temp = arr[start]
        son = 2 * start + 1
        while son <= end:
            if son < end and arr[son] < arr[son + 1]:
                # 找出左右孩子节点较大的
                son += 1
            if temp >= arr[son]:
                # 判断是否为大顶堆
                break
            arr[start] = arr[son]
            # 子节点上移
            start = son
            # 继续向下比较
            son = 2 * son + 1
        arr[start] = temp
        # 将原堆顶插入正确位置

    n = len(lst)
    if n <= 1:
        return lst
    # 建立大顶堆
    root = n // 2 - 1
    # 最后一个非叶节点（完全二叉树中）
    while root >= 0:
        heap_adjust(lst, root, n - 1)
        root -= 1
    # 掐掉堆顶后调整堆
    i = n - 1
    while i >= 0:
        (lst[0], lst[i]) = (lst[i], lst[0])
        # 将大顶堆堆顶数放到最后
        heap_adjust(lst, 0, i - 1)
        # 调整剩余数组成的堆
        i -= 1
    return lst


x = input("请输入待排序的数：")
y = x.split()
arr = []
for i in y:
    arr.append(i)
arr = head_sort(arr)
print("排序结果如下:")
for i in arr:
    print(i, end=" ")
