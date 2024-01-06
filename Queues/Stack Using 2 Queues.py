
from sys import stdin


class Stack :

	#Define data members and __init__()
	def __init__(self):
		self.s1=[]
		self.s2=[]




	'''----------------- Public Functions of Stack -----------------'''


	def getSize(self) :
		#Implement the getSize() function
		return len(self.s1)



	def isEmpty(self) :
		#Implement the isEmpty() function
		return self.getSize()==0



	def push(self, data) :
		#Implement the push(element) function
		while self.s1:
			self.s2.append(self.s1.pop())
		self.s1.append(data)
		while self.s2:
			self.s1.append(self.s2.pop())

			



	def pop(self) :
		#Implement the pop() function
		if self.isEmpty() is True:
			return -1
		return self.s1.pop(0)



	def top(self) :
		#Implement the top() function
		if self.isEmpty() is True:
			return -1
		return self.s1[0]
		




#main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

	inputs = stdin.readline().strip().split(" ")
	choice = int(inputs[0])

	if choice == 1 :
		data = int(inputs[1])
		stack.push(data)

	elif choice == 2 :
		print(stack.pop())

	elif choice == 3 :
		print(stack.top())

	elif choice == 4 : 
		print(stack.getSize())

	else :
		if stack.isEmpty() :
			print("true")
		else :
			print("false")

	q -= 1