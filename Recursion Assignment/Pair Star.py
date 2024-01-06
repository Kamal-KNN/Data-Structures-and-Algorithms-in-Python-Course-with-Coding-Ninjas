from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def res(string):
    if len(string)<=1:
        return string
    if string[0]==string[1]:
        return string[0]+"*"+res(string[1:])
    return string[0]+res(string[1:])
string=input().strip()
print(res(string))
