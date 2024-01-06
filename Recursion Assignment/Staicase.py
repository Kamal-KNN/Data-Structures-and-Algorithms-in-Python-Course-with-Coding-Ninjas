from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def Staircase(n):
    if(n<=3):
        if(n==1):
            return 1
        elif(n==2):
            return 2
        else:
            return 4
    x=Staircase(n-1)
    y=Staircase(n-2)
    z=Staircase(n-3)
    return x+y+z
n=int(input())
a=Staircase(n)
print(a)
