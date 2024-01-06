from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None




	#Your code goes here
def swapNodes(head, index1, index2):
    # If both indices are the same, no need to swap
    if index1 == index2:
        return head

    # Find the nodes at the given indices
    prevX = None
    currX = head
    i = 0
    while currX and i != index1:
        prevX = currX
        currX = currX.next
        i += 1

    prevY = None
    currY = head
    i = 0
    while currY and i != index2:
        prevY = currY
        currY = currY.next
        i += 1

    # If either node is not found in the linked list, return
    if not currX or not currY:
        return head

    # If node at index1 is not the head of the linked list
    if prevX:
        prevX.next = currY
    else:
        head = currY

    # If node at index2 is not the head of the linked list
    if prevY:
        prevY.next = currX
    else:
        head = currX

    # Swap the next pointers of the nodes
    temp = currX.next
    currX.next = currY.next
    currY.next = temp

    return head






























#Taking Input Using Fast I/O
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
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1