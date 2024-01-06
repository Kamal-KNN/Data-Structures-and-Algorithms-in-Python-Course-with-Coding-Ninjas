from os import *
from sys import *
from collections import *
from math import *
def helper(n,k,arr,memo):
    if k==0:
        return True
    if n==0:
        return False
    if memo[n][k]!=-1:
        return memo[n][k]
    if arr[n-1]>k:
        memo[n][k]=helper(n-1,k,arr,memo)
        return memo[n][k]
    memo[n][k]=helper(n-1,k,arr,memo) or helper(n-1,k-arr[n-1],arr,memo)
    return memo[n][k]


def subsetSumToK(n, k, arr):
    memo=list()

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    memo=[[-1]*(k+1)for i in range(n+1)]
    return helper(n,k,arr,memo)
    
    
    

