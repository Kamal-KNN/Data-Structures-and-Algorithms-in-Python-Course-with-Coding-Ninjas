from sys import stdin

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def deleteNode(head, pos) :
    # write your code here !!
    if head is None:
        return head
    if pos ==0:
        return head.next
    count=0
    currHead=head
    while currHead is not None and count <(pos -1):
        count+=1
        currHead=currHead.next
    if (currHead is None) or (currHead.next is None) :
        return head
    currHead.next=currHead.next.next
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
head = takeInput()
pos = int(stdin.readline().rstrip())
head = deleteNode(head, pos)
printLinkedList(head)
