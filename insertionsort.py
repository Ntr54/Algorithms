import math
lst1 = [35,29,65,13,1,205,3]

def insertsort (lst):
    for i in range(1,len(lst1)):
        j = i
        while lst[j] < lst[j-1] and j >= 1:
            lst[j],lst[j-1] = lst[j-1],lst[j]
            j -= 1
            
    return lst

print(insertsort(lst1))