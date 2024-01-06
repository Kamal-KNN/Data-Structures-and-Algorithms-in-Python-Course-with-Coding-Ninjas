from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)
from collections import defaultdict


def getMaxPathSum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    memo = defaultdict(lambda: float('-inf'))
    
    def dfs(row, col):
        if row == n - 1:
            return matrix[row][col]
        
        if memo[row, col] != float('-inf'):
            return memo[row, col]
        
        down = dfs(row + 1, col)
        down_left = dfs(row + 1, col - 1) if col - 1 >= 0 else float('-inf')
        down_right = dfs(row + 1, col + 1) if col + 1 < m else float('-inf')
        
        memo[row, col] = matrix[row][col] + max(down, down_left, down_right)
        return memo[row, col]
    
    max_sum = max(dfs(0, col) for col in range(m))
    return max_sum



    #   Write your code here



























#   taking inpit using fast I/O
def takeInput() :
    n_x = stdin.readline().strip().split(" ")
    n = int(n_x[0].strip())
    m = int(n_x[1].strip())

    matrix=[list(map(int, stdin.readline().strip().split(" "))) for row in range(n)]

    return matrix, n, m


#   main
T = int(input())
while (T > 0):
    T -= 1
    matrix, n, m = takeInput()
    print(getMaxPathSum(matrix))
