from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
def helper(arr,n,target,memo):
    if target==0:
        return 1
    if target<0 or n<=0:
        return 0
    if memo[n][target]!=-1:
        return memo[n][target]
    include=helper(arr,n,target-arr[n-1],memo)
    exclude=helper(arr,n-1,target,memo)
    memo[n][target]=include+exclude
    return memo[n][target]
def countWaysToMakeChange(denominations, value) :
    n=len(denominations)
    memo=[[-1]*(value+1)for i in range(n+1)]
    return helper(denominations,n,value,memo)
    































#taking inpit using fast I/O
def takeInput() :
    numDenominations = int(input())

    denominations = list(map(int, stdin.readline().strip().split(" ")))

    value = int(input())
    return denominations, numDenominations, value


#main
denominations, numDenomination, value = takeInput()
print((countWaysToMakeChange(denominations, value)))