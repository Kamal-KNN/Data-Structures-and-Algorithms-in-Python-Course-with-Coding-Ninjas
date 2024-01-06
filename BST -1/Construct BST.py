import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def sortedarray(arr,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    root=BinaryTreeNode(arr[mid])
    root.left=sortedarray(arr,start,mid-1)
    root.right=sortedarray(arr,mid+1,end)
    return root

def constructBST(lst):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    start=0
    end=len(lst)-1
    root=sortedarray(lst,start,end)
    return root
    

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
if(n>0):
    lst=[int(i) for i in input().strip().split()]
else:
    lst=[]
root=constructBST(lst)
preOrder(root)