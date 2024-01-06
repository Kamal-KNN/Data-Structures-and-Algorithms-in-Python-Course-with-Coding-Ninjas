# Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def findNode(head, n) :
    # Write your code here.
    count=0
    while head:
        if head.data==n:
            return count
        count+=1
        head=head.next
    return -1
        