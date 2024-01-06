from os import *
from sys import *
from collections import *
from math import *

def countDistinctWays(n, memo=dict()):
    # Base cases
    if n == 0:
        return 1
    if n == 1 or n == 2:
        return n

    # Check if the result for 'n' is already memoized
    if memo.get(n, -1) != -1:
        return memo[n]

    # Calculate and memoize the result for 'n'
    memo[n] = (countDistinctWays(n - 1, memo) + countDistinctWays(n - 2, memo)) % (10**9 + 7)
    return memo[n]
