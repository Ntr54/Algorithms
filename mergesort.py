import math
lst1 = [35,29,65,13,1,205,3]
lst2 = [405,379,681,202,273,438,693,901]

def mergesort(lst):
    
    if len(lst) <= 1:
        return lst
    
    lst_left = mergesort(lst[:math.floor(len(lst)/2)])
    lst_right = mergesort(lst[math.floor(len(lst)/2):])

    i_left, i_right = 0,0
    sorted_lst = []
    
    while i_left < len(lst_left) and i_right < len(lst_right):
        if lst_left[i_left] <= lst_right[i_right]:
            sorted_lst.append(lst_left[i_left])
            i_left += 1
        else:
            sorted_lst.append(lst_right[i_right])
            i_right += 1

    if i_left < len(lst_left):
        sorted_lst += lst_left[i_left:]
    elif i_right < len(lst_right):
        sorted_lst += lst_right[i_right:]

    return sorted_lst
print(mergesort(lst2))