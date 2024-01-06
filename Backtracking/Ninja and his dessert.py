from os import *
from sys import *
from collections import *
from math import *

def closestCost(n, m, baseCosts, toppingsCost, target):
    def closest(a, b, target):
        if a == 0:
            return b
        elif b == 0:
            return a
        elif abs(a - target) == abs(b - target):
            return min(a, b)
        elif abs(a - target) < abs(b - target):
            return a
        else:
            return b

    def dfs(topping, index, sum, target):
        if index >= len(topping):
            return sum

        a = dfs(topping, index + 1, sum + topping[index], target)
        b = dfs(topping, index + 1, sum + topping[index] * 2, target)
        c = dfs(topping, index + 1, sum, target)

        return closest(a, closest(b, c, target), target)

    ans = 0

    for i in range(n):
        ans = closest(dfs(toppingsCost, 0, baseCosts[i], target), ans, target)

    return ans