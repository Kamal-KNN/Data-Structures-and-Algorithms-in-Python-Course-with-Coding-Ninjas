from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:

    # Write your code here.
    dp=[0]*(n+1)
    dp[n]=0
    dp[n-1]=abs(heights[n-1]-heights[n-2])
    for i in range(n-2,0,-1):
        dp[i]=min(dp[i+1]+abs(heights[i-1]-heights[i]  ),dp[i+2]+abs(heights[i-1]-heights[i+1]))
    return dp[1]
