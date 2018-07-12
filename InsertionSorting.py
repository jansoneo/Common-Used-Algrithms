# author :yanjx

def InsertionSorting(lst):
    for i in range(1,len(lst)):
        for j in range(i, 0, -1):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]


if __name__== "__main__":
    lst = [2, 3, 1, 4, 6, 3, 2, 235, 8, 1, 13, 2321, 54, 12]
    print(lst)
    InsertionSorting(lst)
    print(lst)