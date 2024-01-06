from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def maximumNonAdjacentSum(nums):    
    # Write your code here.
    prev1=nums[0]
    prev2=0
    for i in range(1,len(nums)):
        include=prev2+nums[i]
        exclude=prev1+0
        ans=max(include,exclude)
        prev2=prev1
        prev1=ans
    return prev1

# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1