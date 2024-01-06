from sys import stdin

def intersection(arr1, arr2, n, m) :

    arr1.sort()
    arr2.sort()

    i = 0 #pointer to iterate over arr1
    j = 0 #pointer to iterate over arr2

    while i < n and j < m :
        
        if arr1[i] == arr2[j] :
            print(arr1[i], end = " ") 
            i += 1
            j += 1
        elif arr1[i] < arr2[j] :
            i += 1
        else :
            j += 1





