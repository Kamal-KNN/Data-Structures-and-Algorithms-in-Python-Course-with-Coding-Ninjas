from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def findSubsetsThatSumToK(arr, n, k) :
    x = []
    def rec(i,n,k,s,r):
        if i==n:
            if s==k:
                x.append(r)
            return
        
        rec(i+1,n,k,s+arr[i],r+[arr[i]])
        rec(i+1,n,k,s,r)
    rec(0,n,k,0,[]) 
    return x





n=int(input())
arr=[int(x) for x in input().split()]
k=int(input())
x=findSubsetsThatSumToK(arr,n,k)

for ele in x:
    print(*ele)
