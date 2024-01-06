from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def subsequence(str,n):
    def helper(str,n,index,x):
        if n==index:
            result.append(x)
            return
        helper(str,n,index+1,x+[str[index]])
        helper(str,n,index+1,x)

    result=[]
    helper(str,n,0,[])
    return result


x=int(input())
str=[int(x)for x in input().split()]
n=len(str)
arr=subsequence(str,n)
for ele in arr:
    print(*ele)
