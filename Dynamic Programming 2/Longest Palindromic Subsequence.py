from os import *
from sys import *
from collections import *
from math import *
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

def longestPalindromeSubsequence(s):
    # Write your code here.
    m=len(s)
    str1=s[::-1]
    n=len(str1)
    memo=[[-1]*(m+1)for i in range(n+1)]
    return helper(s,str1,m,n,memo)
