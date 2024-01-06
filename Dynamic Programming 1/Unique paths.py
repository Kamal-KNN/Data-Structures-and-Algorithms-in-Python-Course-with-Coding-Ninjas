def Count(i,j,mat,dp):
    if i>=0 and j>=0 and mat[i][j]==-1:return 0
    if i==0 and j==0:return 1
    if i<0 or j<0: return 0
    if dp[i][j]!=-1:return dp[i][j]

    up=Count(i-1,j,mat,dp)
    left=Count(i,j-1,mat,dp)
    dp[i][j]=up+left
    return dp[i][j]
def mazeObstacles(n, m, mat):
    dp=[[-1]*m for _ in range(n)]
    return Count(n-1,m-1,mat,dp)%1000000007