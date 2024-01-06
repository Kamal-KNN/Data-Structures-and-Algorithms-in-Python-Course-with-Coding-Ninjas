from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
count=0
def countzeroes(n):
    global count
    if n>0:
        if n%10==0:
            count=count+1
        countzeroes(n//10)
        return count

n=input()
n=int(n)
if n==0:
    print("1")
else:
    print(countzeroes(n))