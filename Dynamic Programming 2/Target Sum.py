from os import *
from sys import *
from collections import *
from math import *

from typing import List
def helper(arr,target,n,memo):
    
    if memo[n][target]!=-1:
        return memo[n][target]
        
    if n==0:
        if target==0:
            return 1
        return 0
    if arr[n-1]>target:
        return helper(arr,target,n-1,memo)
    include=helper(arr,target-arr[n-1],n-1,memo)
    exclude=helper(arr,target,n-1,memo)
    memo[n][target]=include+exclude
    return memo[n][target]

def targetSum(arr: List[int], target: int) -> int:
    total=sum(arr)
    new_target=total+target
    if new_target%2!=0:
        return 0
    new_target//=2
    n=len(arr)
    memo=[[-1]*(new_target+1)for i in range(n+1)]
    return helper(arr,new_target,n,memo)

