from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
def printmid(head):
    slow=head
    fast=head.next
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
    return slow



def bubbleSort(head) :
	#Your code goes here
    if head is None or head.next is None: 
        return head
    current=head
    while current.next is not None:
        runner=current.next
        while runner is not None:
            if current.data>=runner.data:
                current.data,runner.data=runner.data,current.data
            runner=runner.next
        current=current.next
    return head  
































def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head



def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)