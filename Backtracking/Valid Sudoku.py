def Is_safe(x,y,board,n,value):
    for i in range(n):
        if board[i][y]==value or board[x][i]==value:
            return False

    
    # Third condition
    startRow, startCol = 3 * (x // 3), 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if board[startRow + i][startCol + j] == value:
                return False
    return True

def helper(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col]==0:
                for val in range(1,len(matrix)+1):
                    if Is_safe(row,col,matrix,len(matrix),val):
                        matrix[row][col]=val
                        if helper(matrix):
                            return True
                        else:
                            matrix[row][col]=0
                return False
    return True
                    

def isItSudoku(matrix):
    ans=helper(matrix)
    return ans