from math import *
from collections import *
from sys import *
from os import *

def multiplyNumbers(m,n):
    if m==0 or n==0:
        return 0
    
    if n>0:
        smallAns=multiplyNumbers(m,n-1)
        return smallAns+m
    else:
        smallAns=multiplyNumbers(m,n+1)
        return smallAns-m
from sys import setrecursionlimit
setrecursionlimit(11000)
m=int(input())
n=int(input())
print(multiplyNumbers(m,n))
    