# author:yanjx


def FastSort(lst, begin, end):
    """
    快速排序Python实现
    """

    if begin < end:
        i, j = begin, end
        key = lst[begin]
        while i < j:
            while i < j and key <= lst[j]:
               j -= 1
            if i < j:
                lst[i] = lst[j] # 将一边找出的元素赋值给另一边
                i += 1
            while i < j and key >= lst[i]:
                i += 1
            if i < j:
                lst[j] = lst[i]
                j -= 1
        lst[i] = key    # 最后i=j，且等于最后一次找到的元素， 所以要把key赋值给它，这就是key再整个有序数组中的位置了
        FastSort(lst, begin, i-1)
        FastSort(lst, i+1, end)


if __name__ == "__main__":
    lst = [2, 3, 1, 4, 6, 3, 2, 235, 8, 1, 13, 2321, 54, 12]
    print(lst)
    FastSort(lst, 0, len(lst)-1)
    print(lst)
