from os import *
from sys import *
from collections import *
from math import *

class Queue:
    # Stacks to be used in the operations.
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    # Enqueues 'X' into the queue. Returns true after enqueuing.
    def enqueue(self, X):
        # Write your code here
        self.stk1.append(X)
        return True

    """
      Dequeues top element from queue. Returns -1 if the queue is empty, 
      otherwise returns the popped element.
    """
    def dequeue(self):
        # Write your code here
        if len(self.stk1)==0:
            return -1
        while len(self.stk1)!=0:
            self.stk2.append(self.stk1.pop())
        data=self.stk2.pop()
        while len(self.stk2)!=0:
            self.stk1.append(self.stk2.pop())
        return data