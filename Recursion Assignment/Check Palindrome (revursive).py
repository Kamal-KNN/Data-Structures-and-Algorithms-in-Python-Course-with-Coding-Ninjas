from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def isPalindrome(string):
    if len(string)<=1:
        return True
    if string[0]!=string[len(string)-1]:
        return False
    return isPalindrome(string[1:-1])
  
