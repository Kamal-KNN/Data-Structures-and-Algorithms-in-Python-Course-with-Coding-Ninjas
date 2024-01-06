def addSolution(n, ans, row):
    currans = []
    for i in range(n):
        for j in range(n):
            if row[j] == i:
                currans.append(1)
            else:
                currans.append(0)
    ans.append(currans)

def solve(col, n, ans, row, d1, d2):
    if col == n:
        return addSolution(n, ans, row)
    for i in range(n):
        if((row[i] == -1) and (d1[col-i+n-1] == -1) and (d2[col+i] == -1)):
            row[i] = d1[col-i+n-1] = d2[col+i] = col
            solve(col+1, n, ans, row, d1, d2)
            row[i] = d1[col-i+n-1] = d2[col+i] = -1


def solveNQueens(n):
    # Write your code here.
    ans = []
    row = [-1] * 30
    d1 = [-1] * 30
    d2 = [-1] * 30
    solve(0, n, ans, row, d1, d2)
    return ans
    pass








# def solve_n_Queens(board,row,N):
#     if row==N:
#         return True
#     for col in range(N):
#         if is_safe_to_place_queen(board,row,col,N):
#             board[row][col]=1
#             if solve_n_Queens(board,row+1,N):
#                 return True
#             board[row][col]=0
#     return False
# def is_safe_to_place_queen(board,row,col,n):
#     for i in range(row):
#         if board[i][col]==1:   # checking for same column
#             return False
#     # checking for left upper diagonal
#     for i,j in zip( range(row,-1,-1), range(col,-1,-1)):
#         if board[i][j]==1:
#             return False
#     for i,j in zip( range(row,-1,-1), range(col,n) ):
#         if board[i][j]==1:
#             return False
#     return True
    
   
   


# def solveNQueens(n):
#     # Write your code here.
#     board=[[0]*n for i in range(n)]
#     if solve_n_Queens(board,0,n) is True:
#         return board 
