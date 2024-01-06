from os import *
from sys import *
from collections import *
from math import *

def houseRobber(valueInHouse):
    # Write your function here.
    def findmax(arr):
        if not arr:
            return 0
        if len(arr)<=2:
            return max(arr)
        dp=[0]*len(arr)
        dp[0]=arr[0]
        dp[1]=max(arr[0],arr[1])
        for i in range(2,len(arr)):
            dp[i]=max(dp[i-1],dp[i-2]+arr[i]  )
        return dp[-1]
    if len(valueInHouse)<=3:
        return max(valueInHouse)
    ans1=findmax(valueInHouse[1:])
    ans2=findmax(valueInHouse[:-1])
    return max(ans1,ans2)