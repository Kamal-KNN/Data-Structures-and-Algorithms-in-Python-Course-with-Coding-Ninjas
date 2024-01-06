from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def keypad(n):
    if not n:
        return []
    key={
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz",

    }
    def backtracking(combination,next_digit):
        if not next_digit:
            print(combination)
            return
        current_digit=next_digit[0]
        letters=key[current_digit]
        for letter in letters:
            backtracking(combination+letter,next_digit[1:])
    n=str(n)    
    backtracking("",n)





n=int(input())
keypad(n)
