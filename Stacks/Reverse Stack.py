from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


def reverseStack(s1,s2):
    if len(s1) == 0 or len(s1) == 1:
        return 
    
    x = s1[-1]
    s1.pop()
    
    reverseStack(s1, s2)
    while len(s1) > 0:
        s2.append(s1[-1])
        s1.pop()
    
    s1.append(x)
    
    while len(s2) > 0:
        s1.append(s2[-1])
        s2.pop()
    
    return s1






























'''-------------- Utility Functions --------------'''

#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Taking input using fast I/o method
def takeInput() :
	size = int(stdin.readline().strip())
	inputStack = list()

	if size == 0 :
		return inputStack


	values = list(map(int, stdin.readline().strip().split(" ")))
	inputStack = values

	return inputStack


# Main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack) :
	print(inputStack.pop(), end = " ")