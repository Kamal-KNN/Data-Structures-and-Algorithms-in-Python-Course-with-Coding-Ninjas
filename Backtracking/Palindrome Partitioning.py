from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import json
def is_safe(s,start,end):
    while start<end:
        if s[start]!=s[end]:
            return False
        start+=1
        end-=1
    return True

def partition(s):
    # Write your code here.
    def backtrack(start):
        if start==len(s):
            partitions.append(current_partition.copy())
            return
        for end in range(start,len(s)):
            if is_safe(s,start,end):
                current_partition.append(s[start:end+1])
                backtrack(end+1)
                current_partition.pop()


    partitions=[]
    current_partition=[]
    backtrack(0)
    return partitions

s=stdin.readline().rstrip()

final=partition(s)

for ele in final:
    ele = sorted(ele)
    print(json.dumps(ele))
