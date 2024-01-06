from os import *
from sys import *
from collections import *
from math import *
def issafe(arr, row, col, n):
    return 0 <= row < n and 0 <= col < n and  arr[row][col] == 1
def backtracking(x,y,n,arr,path,ans,moves):
    if x==y==n-1:
        ans.append(path)
        return
    for dx,dy,move in moves:
        start_x=x+dx
        start_y=y+dy
        if issafe(arr,start_x,start_y,n):
            arr[x][y]=0
            backtracking(start_x,start_y,n,arr,path+[move],ans,moves)
            arr[x][y]=1


def searchMaze(arr, n):
    # Write your code here.
    ans=[]
    if arr[0][0]==0:
        return ans
    moves=[(1,0,"D"),(0,-1,"L"),(0,1,"R"),(-1,0,"U")]
    backtracking(0,0,n,arr,[],ans,moves)
    kamal=[]
    for path in ans:
        kamal.append("".join(path))
    return kamal
    
