from os import *
from sys import *
from collections import *
from math import *

from typing import List
def helper(arr,target,memo):
    if target==0:
        return 0
    if memo[target]!=-1:
        return memo[target]
    min_coins=float('inf')
    for coins in arr:
        if target-coins>=0:
            num_coins=helper(arr,target-coins,memo)
            if num_coins !=-1:
                min_coins=min(min_coins,num_coins+1)
    memo[target]=-1 if min_coins==float('inf')else min_coins
    return memo[target]

def minimumElements(num: List[int], x: int) -> int:
    # Write your code here.
    memo=[-1]*(x+1)
    memo[0]=0
    return helper(num,x,memo)
    