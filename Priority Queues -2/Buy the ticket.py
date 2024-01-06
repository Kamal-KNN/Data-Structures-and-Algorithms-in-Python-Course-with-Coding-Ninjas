from sys import stdin
import sys
import heapq as heap

class LinkedListNode :
    def __init__(self, data) :
        self.data = data
        self.next = None
        
class Queue :
    def __init__(self) :
        self.head = None 
        self.tail = None
        self.size = 0
        
    def enqueue(self, data) :
        newNode = LinkedListNode(data)
        if self.head is None :
            self.head = self.tail = newNode
        else :
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        return
        
    def dequeue(self) :
        if self.head is None :
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    
    def getSize(self) :
        return self.size
    
    def isEmpty(self) :
        if self.head is None :
            return True
        return False
    
    def peek(self) :
        if self.head is None :
            return None
        return self.head.data
    
def buyTicket(arr, n, k):
    maxHeap = []
    for i in arr:
        heap.heappush(maxHeap, -i)  # Use negative values for max heap

    queue = Queue()
    for i in range(n):
        queue.enqueue(i)

    time = 0
    while not queue.isEmpty():
        if -maxHeap[0] == arr[queue.peek()]:
            if queue.peek() == k:
                return time + 1
            heap.heappop(maxHeap)
            queue.dequeue()
            time += 1
        else:
            queue.enqueue(queue.dequeue())

#taking input using fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return n, list(), int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    k = int(stdin.readline().strip())
    return n, arr, k

#main
sys.setrecursionlimit(10**6)
n, arr, k = takeInput()
print(buyTicket(arr, n, k))