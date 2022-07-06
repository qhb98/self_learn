# 快速排序
"""
1.从数列中挑出一个元素，称为“基准”pivot
2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区partition操作。
3.递归地recursive把小于基准值元素的子数列和大于基准值元素的子数列排序。

"""


def quick_sort(lst):
    # 此函数用于完成分区操作
    def partition(arr, left, right):
        key = left
        # 划分参考数索引，默认第一个数为基准数
        while left < right:
            # 如果列表后面的数，比基准数大或相等，则前移一位直到有比基准数小的数出现
            while left < right and arr[right] >= arr[key]:
                right -= 1
            # 如果列表前边的数，比基准数小或相等，则后移一位直到比基准数大的数出现
            while left < right and arr[left] <= arr[key]:
                left += 1
            # 此时已找到一个比基准大的数，和一个比基准小的数，将他们互换
            (arr[left], arr[right]) = (arr[right], arr[left])

        # 当从两边分别逼近，直到两个位置相等时结束，将左边小的同基准进行交换
        (arr[left], arr[key]) = (arr[key], arr[left])
        # 返回目前基准所在位置的索引
        return left

    def quicksort(arr, left, right):
        if left >= right:
            return None
        # 从基准开始分区
        mid = partition(arr, left, right)
        # 递归调用
        # print(arr)
        quicksort(arr, left, mid - 1)
        quicksort(arr, mid + 1, right)

    # 主函数
    n = len(lst)
    if n <= 1:
        return lst
    quicksort(lst, 0, n - 1)
    return lst


x = input("请输入待排序的数: ")
y = x.split()
arr = []
for i in y:
    arr.append(i)
arr = quick_sort(arr)
print("排序结果如下：")
for i in arr:
    print(i, end=" ")
