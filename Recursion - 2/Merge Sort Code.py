def merge(arr: [int] , l: int, m: int, r: int):
    num1=m-l+1
    num2=r-m

    L= [None]* num1
    R= [None]* num2

    for i in range(num1):
        L[i]=arr[l+i]
    for j in range(num2):
        R[j]= arr[m+1+j]

    i=0
    j=0
    k=l
    while i< num1 and j< num2:
        if L[i] < R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    while i< num1:
        arr[k]=L[i]
        i+=1
        k+=1
    while j< num2:
        arr[k]= R[j]
        j+=1
        k+=1
def mergeSort(arr:[int], l: int, r:int):
    if l<r:
        m=(l+r)//2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)

        merge(arr,l,m,r)
