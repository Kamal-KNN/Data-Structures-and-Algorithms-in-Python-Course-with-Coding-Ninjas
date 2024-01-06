from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def kamal(n):
    if n<10:
        return n
    output=n%10+kamal(n//10)
    return output
n=int(input())
print(kamal(n))
