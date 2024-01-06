from os import *
from sys import *
from collections import *
from math import *

def helper(s,t,m,n,memo):
	if m==0 or n==0:
		return ""
	if memo[n][m]!=-1:
		return memo[n][m]
	if s[m-1]==t[n-1]:
		memo[n][m]= s[m-1]+helper(s[:m-1],t[:n-1],m-1,n-1,memo)
		return memo[n][m]
	lcs1=helper(s[:m-1],t,m-1,n,memo)
	lcs2=helper(s,t[:n-1],m,n-1,memo)
	if len(lcs1)>len(lcs2):
		memo[n][m]=lcs1
	else:
		memo[n][m]=lcs2
	return memo[n][m]

def shortestSupersequence(a: str, b: str) -> str:
	# Write your code here.
    i,j=0,0
    m=len(a)
    n=len(b)
    memo=[[-1]*(m+1)for i in range(n+1)]
    result=helper(a,b,m,n,memo)
    result=result[::-1]
    ans=""
    for num in result:
        while i<m and a[i]!=num:
            ans+=a[i]
            i+=1
        while j<n and b[j]!=num:
            ans+=b[j]
            j+=1
        ans+=num
        i+=1
        j+=1
    ans+=a[i:]
    ans+=b[j:]
    return ans
