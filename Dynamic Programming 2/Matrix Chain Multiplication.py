from os import *
from sys import *
from collections import *
from math import *
def helper(arr,i,j,memo):
	if i==j:
		return 0
	if memo[i][j]!=-1:
		return memo[i][j]
	min_cost=float('inf')
	for k in range(i,j):
		left=helper(arr,i,k,memo)
		right=helper(arr,k+1,j,memo)
		cost=arr[i-1]*arr[k]*arr[j]
		min_cost=min(min_cost,cost+left+right)
		memo[i][j]=min_cost
	return memo[i][j]

def matrixMultiplication(arr, n):
	# Write your code here.
	memo=[[-1]*n for i in range(n)]

	return helper(arr,1,n-1,memo)

	