
from sys import stdin


def isBalanced(expression) :
	#Your code goes here
	stack=[]
	for char in expression:
		if char in "({[":
			stack.append(char)
		elif char=="]":
			if not stack or stack[-1]!="[":
				return False
			stack.pop()
		elif char=="}":
			if not stack or stack[-1]!='{':
				return False
			stack.pop()
		elif char==")":
			if not stack or stack[-1]!="(":
				return False
			stack.pop()
	if  stack:
		return False
	return True


























	




#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")
