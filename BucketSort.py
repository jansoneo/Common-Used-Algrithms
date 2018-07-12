 # author: yanjx

def BucketSort(lst):
    """
    Implement of Bucket sort with dictionary in Python.
    """
    lst_dict = {}
    for i in range(max(lst)+1): # 先建立好桶(key)
        lst_dict[i] = 0

    for i in lst:
        if i in lst_dict.keys():
            lst_dict[i] += 1    # 往桶中装数
    result = []
    for ele in lst_dict:
        for i in range(lst_dict[ele]):
            result.append(ele)

    return result

if __name__ == "__main__":
    lst = [2, 3, 1, 4, 6, 3, 2, 235, 8, 1, 13, 2321, 54, 12]
    print(lst)
    Sorted_lst =  BucketSort(lst)
    print(Sorted_lst)