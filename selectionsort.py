import math
lst1 = [35,29,65,13,1,205,3]
lst2 = [405,379,681,202,273,438,693,901]

def selectionsort(lst):
    for i in range(len(lst)-1,-1,-1):
        greatest = 0
        for j in range(i+1):
            if lst[j] > lst[greatest]:
                greatest = j
        lst[i],lst[greatest] = lst[greatest],lst[i]
    return lst

print(selectionsort(lst2))