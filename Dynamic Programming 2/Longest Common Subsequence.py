
from sys import stdin
def helper(s,t,m,n,memo):
	if m==0 or n==0:
		return 0
	if memo[n][m]!=-1:
		return memo[n][m]
	if s[m-1]==t[n-1]:
		memo[n][m]= 1+helper(s[:m-1],t[:n-1],m-1,n-1,memo)
		return memo[n][m]
	memo[n][m]= max(helper(s[:m-1],t,m-1,n,memo),helper(s,t[:n-1],m,n-1,memo))
	return memo[n][m]


def lcs(s, t) :
	#Your code goes here
	m=len(s)
	n=len(t)
	memo=[[-1]*(m+1)for i in range(n+1)]
	return helper(s,t,m,n,memo)






























    


#main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(lcs(s, t))