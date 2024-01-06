from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def Gsum(k):
    if k==0:
        return 1
    return 1/2**k + Gsum(k-1)

k = int(input())
print (str.format('{0:.5f}',Gsum(k)))
