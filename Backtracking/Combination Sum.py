
from typing import List
from copy import copy

def combSum(ARR,B):
    ARR.sort()
    def backtrack(start,current_sum,total,):
        if total==B:
            result.append(current_sum.copy())
            return
        if start>=len(ARR) or total>B:
            return
        current_sum.append(ARR[start])
        backtrack(start,current_sum,total+ARR[start])
        current_sum.pop()
        backtrack(start+1,current_sum,total)

    

    result=[]
    current_sum=[]
    backtrack(0,current_sum,total=0)
    result.sort()
    return result