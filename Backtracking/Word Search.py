from typing import List

from typing import List
def new_function(list,word):
    def dfs(i,j,k):
        if not (0<=i<len(list)) or not (0<=j<len(list[0])) or list[i][j]!=word[k]:
            return False
        if k==len(word)-1:
            return True
        temp,list[i][j]=list[i][j],"/"
        found=dfs(i+1,j,k+1)or dfs(i,j-1,k+1) or dfs(i,j+1,k+1) or dfs(i-1,j,k+1)
        list[i][j]=temp
        return found
    for row in range(len(list)):
        for col in range(len(list[0])):
            if dfs(row,col,0):
                return True
    return False

def present(board: List[List[str]], word: str, n: int, m: int) -> bool:
    # Write your code here
    if new_function(board,word):
        return True
    else:
        return False

     