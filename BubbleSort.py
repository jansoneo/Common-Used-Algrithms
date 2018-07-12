
# author: yajx


def BubbleSort(lst):
    """
    冒泡排序Python实现
    """
    l = len(lst)
    for i in range(1, l):
        for j in range(l-1, i-1, -1):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst


if __name__ == "__main__":
    lst = [2, 3, 1, 4, 6, 3, 2, 235, 8, 1, 13, 2321, 54, 12]
    print(lst)
    print(BubbleSort(lst))
