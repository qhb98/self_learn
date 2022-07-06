# 二分查找


def binary_search(lst, item):
    first = 0
    last = len(lst) - 1
    while first <= last:
        midpoint = (first + last) // 2
