from os import *
from sys import *
from collections import *
from math import *

from typing import List
def helper(arr,target,n,memo):
    if target<0:
        return 0
    if memo[n][target]!=-1:
        return memo[n][target]


    if n==0:
        if target==0:
            return 1
        return 0
    include=helper(arr,target-arr[n-1],n-1,memo)
    exclude=helper(arr,target,n-1,memo)
    memo[n][target]= include+exclude
    return memo[n][target]



def countPartitions(n: int, d: int, arr: List[int]) -> int:
    # write your code here
    MOD=(10**9+7)
    total=sum(arr)
    k=total-d
    if k%2 or d>total:
        return 0
    k//=2
    memo=[[-1]*(k+1)for i in range(n+1)]
    return helper(arr,k,n,memo)%MOD
