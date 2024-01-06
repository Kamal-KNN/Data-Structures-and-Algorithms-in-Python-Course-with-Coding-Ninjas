from sys import stdin
from sys import maxsize as MAX_VALUE



def countMinStepsToOne(n) :
    dp=[0]*(n+1)
    for i in range(2,n+1):
        dp[i]=dp[i-1]+1
        if i%2==0:
            dp[i]=min(dp[i],dp[i//2]+1)
        if i%3==0:
            dp[i]=min(dp[i],dp[i//3]+1)
    return dp[n]





#main
n = int(stdin.readline().rstrip())
print(countMinStepsToOne(n))