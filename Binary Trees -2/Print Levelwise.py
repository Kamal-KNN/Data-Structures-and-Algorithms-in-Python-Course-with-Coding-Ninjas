from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise(root):
    # Your code goes here
    q=queue.Queue()
    if root is None:
        return
    q.put(root)
    while (not(q.empty())):
        current_node=q.get()
        print(current_node.data,end=":")
        if current_node.left is not None:
            print("L:",end="")
            print(current_node.left.data,end=",")
            q.put(current_node.left)
        else:
            print("L:",end="")
            print(-1,end=",")

        if current_node.right is not None:
            print("R:",end="")
            print(current_node.right.data)
            q.put(current_node.right)
        else:
            print("R:",end="")
            print(-1)
        































    



#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root


# Main
root = takeInput()
printLevelWise(root)