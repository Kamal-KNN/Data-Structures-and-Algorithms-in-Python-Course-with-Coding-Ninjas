from sys import stdin


def rotate(arr, n, d):
    #Your code goes here
    d=n-d
    def reverse(arr,low,high):
        while low<high:
            arr[low],arr[high]=arr[high],arr[low]
            low+=1
            high-=1
    
    reverse(arr,0,n-d-1)
    reverse(arr,n-d,n-1)
    reverse(arr,0,n-1)
    


























#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1