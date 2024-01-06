from sys import stdin
import sys 
import bisect
sys.setrecursionlimit(10**7)
def longestIncreasingSubsequence(arr, n) :
    tails=[]
    for num in arr:
        index=bisect.bisect_left(tails,num)
        if index==len(tails):
            tails.append(num)
        else:
            tails[index]=num



	# Your code goes here
    return len(tails)































#taking inpit using fast I/O
def takeInput() :
    n = int(input())

    if n==0 :
        return list(), n
        
    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(longestIncreasingSubsequence(arr, n))