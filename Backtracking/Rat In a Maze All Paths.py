from os import *
from sys import *
from collections import *
from math import *

def isSafe(x, y, n, visited, maze):
    if 0 <= x < n and 0 <= y < n and visited[x][y] == 0 and maze[x][y] == 1:
        return True
    else:
        return False

def solve(maze, n, ans, x, y, moves, visited):
    if x == n - 1 and y == n - 1:
        visited[x][y] = 1
        temp = []
        for i in range(n):
            for j in range(n):
                temp.append(visited[i][j])
        ans.append(temp)
        visited[x][y] = 0
        return

    visited[x][y] = 1
    for row, col in moves:
        dx = x + row
        dy = y + col
        if isSafe(dx, dy, n, visited, maze):
            solve(maze, n, ans, dx, dy, moves, visited)
            visited[dx][dy] = 0  # Backtrack

def ratInAMaze(maze, n):
    # Write your code here.
    moves = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    visited = [[0] * n for i in range(n)]
    ans = []
    solve(maze, n, ans, 0, 0, moves, visited)
    for path in ans:
        print(*path)

# Main.
n = int(input())
maze = n*[0]

for i in range(0 , n):
    maze[i]=input().split()
    maze[i]=[int(j) for j in maze[i]]
    
ratInAMaze(maze , n) 
