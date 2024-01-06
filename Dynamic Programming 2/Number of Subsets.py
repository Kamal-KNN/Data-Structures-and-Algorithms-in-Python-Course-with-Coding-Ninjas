from typing import List

def findWays(arr: List[int], k: int) -> int:
    # Write your code here.
    n=len(arr)
    dp=[[0 for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0]=1
    
    for j in range(1,k+1):
        dp[0][j]=0
    
    for i in range(1,n+1):
        for j in range(k+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j]+dp[i-1][j-arr[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][k]%(10**9+7)