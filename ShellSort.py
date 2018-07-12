# author:yanjx

def ShellSort(lst):
    i = len(lst)//2
    while i >0:
        for j in range(i,len(lst)):
            for k in range(j, i-1, -i): # 此处需要主要一下，当j=i的时候这里不执行，所以要i-1，这时j正好可以执行到i
                if lst[k] < lst[k-i]:
                    tmp = lst[k]
                    lst[k] = lst[k-i]
                    lst[k-i] = tmp

        i//=2

if __name__== "__main__":
    lst = [2, 3, 1, 4, 6, 3, 2, 235, 8, 1, 13, 2321, 54, 12]
    print(lst)
    ShellSort(lst)
    print(lst)