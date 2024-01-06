from sys import stdin
import sys

def cutRod(price, n):

    # Write your code here.
    max_values=[0]*(n+1)
    for i in range(1,n+1):
        max_value=0
        for j in range(1,i+1):
            max_value=max(max_value,price[j-1]  + max_values[i-j]   )
        max_values[i]=max_value
    return max_values[n]

# Taking input using fast I/O.
def takeInput():
    n = int(input())

    price = list(map(int, input().strip().split(" ")))

    return price, n


# Main.
t = int(input())
while t:
    price, n = takeInput()
    print(cutRod(price, n))
    t = t-1
