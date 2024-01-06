from sys import stdin


def findDuplicate(arr, n) :
    result=0
    #Your code goes here
    l=len(arr)
    for i in range(0,n-1):
        result^=i
        result^=arr[i]
    return result^arr[l-1]
    




























    



#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip()) 

while t > 0 :

    arr, n = takeInput()
    print(findDuplicate(arr, n))

    t -= 1