# 计数排序


def count_sort(lst):
    n = len(lst)
    num = max(lst)
    count = [0] * (num + 1)
    for i in range(0, n):
        count[lst[i]] += 1
    arr = []
    for i in range(0, num + 1):
        for j in range(0, count[i]):
            arr.append(i)
    return arr


x = input("请输入待排序的数：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = count_sort(arr)
# print(arr)
print("排序结果如下：")
for i in arr:
    print(i, end=" ")
