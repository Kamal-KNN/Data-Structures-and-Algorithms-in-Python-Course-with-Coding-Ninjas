from sys import stdin

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def mergeTwoSortedLinkedLists(head1, head2):
    # Write your code here
    dumy=Node(0)
    curr=dumy
    while head1 and head2:
        if head1.data<=head2.data:
            curr.next=head1
            curr=curr.next
            head1=head1.next
        else:
            curr.next=head2
            curr=curr.next
            head2=head2.next
        
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


# Main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head1 = takeInput()
    head2 = takeInput()

    newHead = mergeTwoSortedLinkedLists(head1, head2)
    printLinkedList(newHead)

    t -= 1