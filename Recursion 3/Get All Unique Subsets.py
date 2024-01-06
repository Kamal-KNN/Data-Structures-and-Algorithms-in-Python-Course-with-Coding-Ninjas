from math import *
from collections import *
from sys import *
from os import *
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # write the code  logic here !!! 
        def backtrack(start, subset):
            unique_subsets.add(tuple(subset))
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        unique_subsets = set()
        backtrack(0, [])
        return [list(x) for x in unique_subsets]


if __name__ == "__main__":
    n= int (input())
    nums=list(map(int, input().split()))  
    obj = Solution()
    ans = obj.subsetsWithDup(nums)
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()