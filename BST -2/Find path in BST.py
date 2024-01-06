import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findPathBST(root,data):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return
    if root.data==data:
        lst=list()
        lst.append(root.data)
        return lst
    lefttree=findPathBST(root.left,data)
    if lefttree is not None:
        lefttree.append(root.data)
        return lefttree
    righttree=findPathBST(root.right,data)
    if righttree is not None:
        righttree.append(root.data)
        return righttree
    else:
        return None

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
data = int(input())
path = findPathBST(root,data)
if path is not None:
    for ele in path:
        print(ele,end=' ')