# 顺序查找
"""
1.

"""


def sequence_sort(lst, v):
    for k in range(len(lst)):
        if lst[k] == v:
            return k
    return -1


if __name__ == "__main__":
    x = input("请输入待查找的数列:")
    y = x.split()
    arr = []
    for i in y:
        arr.append(i)
    a = input("请输入要查找的数:")
    v_find = sequence_sort(arr, a)
    print(v_find)
