## Read input as specified in the question.
## Print output as specified in the question.
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkCousins(root,p,q):
    #Implement Your Code Here
    return not is_siblings(root, p, q) and level(root, 0, p) == level(root, 0, q)
def is_siblings(root, node1, node2):
    if not root:
        return False
    if root.left and root.right:
        if root.left.data == node1 and root.right.data == node2:
            return True
    return is_siblings(root.left, node1, node2) or is_siblings(root.right, node1, node2)
def level(root, k, node1):
    if not root:
        return -1
    if root.data == node1:
        return k
    left = level(root.left, k + 1, node1)
    right = level(root.right, k + 1, node1)
    if left == -1:
        return right
    if right == -1:
        return left
    return -1

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
p = int(input())
q = int(input())
ans = checkCousins(root,p,q)
if ans is True:
    print('true')
else:
    print('false')
