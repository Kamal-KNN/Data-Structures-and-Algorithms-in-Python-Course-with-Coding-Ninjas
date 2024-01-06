from os import *
from sys import *
from collections import *
from math import *

def maximumProduct(arr, n):
    # write your code here
    # Return an integer denoting the answer to the required problem 
    ans=float('-inf')
    product_left=1
    product_right=1
    for i in range(n):
        product_left*=arr[i]
        product_right*=arr[n-1-i]
        ans=max(ans,max(product_left,product_right))
        if product_left==0:
            product_left=1
        if product_right==0:
            product_right=1
    return ans

    