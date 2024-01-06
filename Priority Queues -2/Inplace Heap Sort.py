
def heapify(arr,n,i):
    smallest=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[left]>arr[smallest]:
        smallest=left
    if right<n and arr[right]>arr[smallest]:
        smallest=right
    if smallest!=i:
        arr[smallest],arr[i]=arr[i],arr[smallest]
        heapify(arr,n,smallest)
def heapSort(arr):
    n=len(arr)
    for i in range((n//2)-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)
    return arr

n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr[::-1]:
    print(ele,end=' ')