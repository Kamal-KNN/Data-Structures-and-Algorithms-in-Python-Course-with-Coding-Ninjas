from os import *
from sys import *
from collections import *
from math import *
def knapsack_problem(values,weight,capacity,n,memo):
    if n==0 or capacity==0:
        return 0
    if memo[n][capacity]!=-1:
        return memo[n][capacity]
    if weight[n-1]>capacity:
        memo[n][capacity]= knapsack_problem(values,weight,capacity,n-1,memo)
        return memo[n][capacity]
    include=values[n-1]+knapsack_problem(values,weight,capacity-weight[n-1],n-1,memo)
    exclude=knapsack_problem(values,weight,capacity,n-1,memo)
    memo[n][capacity]= max(include,exclude)
    return memo[n][capacity]



## Read input as specified in the question.
## Print output as specified in the question.
t=int(input())
while t:
    N=int(input())
    weight=list(map(int,input().split()))
    values=list(map(int,input().split()))
    capacity=int(input())
    memo=[[-1]*(capacity+1 )  for i in range(N+1)]
    print(knapsack_problem(values,weight,capacity,N,memo))

    
    t-=1