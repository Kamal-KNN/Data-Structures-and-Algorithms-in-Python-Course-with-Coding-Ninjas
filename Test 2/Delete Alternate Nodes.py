''' 
    Following is the node structure

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

'''

def deleteAlternateNodes(head):
    # Write your code here
    while head.next is not None:
        if head.next.next is not None:
            head.next=head.next.next
            head=head.next
        else:
            head.next=None