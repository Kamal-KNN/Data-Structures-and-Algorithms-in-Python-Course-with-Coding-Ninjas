from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

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



def mergeSort(head) :
	#Your code goes here
    if head is None or head.next is None:
        return head
    mid=printmid(head)
    head1=mid.next
    mid.next=None
    left_part=mergeSort(head)
    right_part=mergeSort(head1)
    sorted_list=merge(left_part,right_part)
    return sorted_list
def merge(head1,head2):
    dumy=Node(0)
    curr=dumy
    while head1 is not None and head2 is not None:
        if head1.data<=head2.data:
            curr.next=head1
            head1=head1.next
            curr=curr.next
        else:
            curr.next=head2
            head2=head2.next
            curr=curr.next
    while head1 is not None:
        curr.next=head1
        head1=head1.next
        curr=curr.next
    while head2 is not None:
        curr.next=head2
        head2=head2.next
        curr=curr.next
    return dumy.next





























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

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1