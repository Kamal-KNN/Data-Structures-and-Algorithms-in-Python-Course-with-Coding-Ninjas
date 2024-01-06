
from sys import stdin

def stockSpan(price, n) :
	#Your code goes here
    stk=list()
    output=[-1]*n
    stk.append(0)
    output[0]=1
    for i in range(1,n):
        while (not isEmpty(stk)) and (price[top(stk)] < price[i]):
            stk.pop()
        if isEmpty(stk):
            output[i]=i+1
        else:
            output[i]=i-top(stk)
        stk.append(i)
    return output
def isEmpty(stack):
    return len(stack)==0
def top(stack):
    return stack[len(stack)-1]


#'''-------------- Utility Functions --------------'''




def printList(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = " ")

	print()


def takeInput():
	size = int(stdin.readline().strip())

	if size == 0 :
		return list(), 0

	price = list(map(int, stdin.readline().strip().split(" ")))

	return price, size


#main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)
