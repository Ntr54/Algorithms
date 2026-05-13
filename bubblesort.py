import math
lst1 = [35,29,65,13,1,205,3]

def bbsort(lst):
    print(lst)
    for i in range(len(lst)-1,-1,-1):
        for j in range(0,i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
            print(lst)
    return lst

bbsort(lst1)