import sys
sys.setrecursionlimit(10 ** 8)


def subsetsSumK(arr, k) :
    #Your code goes here
    result=[]
    def helper(arr,n,target,index,temp_sum,x):
        # base
        if index==n:
            if target==temp_sum:
                result.append(x)
            return
        helper(arr,n,target,index+1,temp_sum+arr[index],x+[arr[index]])
        helper(arr,n,target,index+1,temp_sum,x)
    n=len(arr)
    helper(arr,n,k,0,0,[])
    return result






















#taking input
def takeInput() :
    n = int(input().strip())

    if n == 0 :
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr, n


#printing the list of lists
def printListOfList(liOfLi) :
    for li in liOfLi :
        for elem in li :
            print(elem, end = " ")
        print()

#main
arr, n = takeInput()

if n != 0 :
    k = int(input().strip())
    liOfLi = subsetsSumK(arr, k)

    printListOfList(liOfLi)

