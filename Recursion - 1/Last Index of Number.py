from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def lastindex(arr,target):
    if len(arr)==0:
        return -1
    smallerlist=arr[1:]
    output=lastindex(smallerlist,target)
    if output!=-1:
        return output+1
    else:
        if arr[0]==target:
            return 0
        else:
            return -1
size=int(input())
arr=[int(i) for i in input().split()]
target=int(input())
print(lastindex(arr,target))


    