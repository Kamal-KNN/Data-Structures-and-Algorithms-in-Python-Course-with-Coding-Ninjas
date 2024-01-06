from os import *
from sys import *
from collections import *
from math import *
def solve(triangle,row,col,memo):
    if row==len(triangle)-1:
        return triangle[row][col]
    if memo[row][col] is not None:
        return memo[row][col]
    down=solve(triangle,row+1,col,memo)
    down_right=solve(triangle,row+1,col+1,memo)
    min_sum=triangle[row][col]+min(down,down_right)
    memo[row][col]=min_sum
    return min_sum

def minimumPathSum(triangle, n):
    # Write your code here.
    memo=[[None for _ in range(n)]for i in range(n)]
    return solve(triangle,0,0,memo)
    