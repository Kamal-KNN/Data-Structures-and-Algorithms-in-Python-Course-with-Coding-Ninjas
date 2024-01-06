## Read input as specified in the question.
## Print output as specified in the question.
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def longestPath(root):
    if root is None:
        return []

    left_path = longestPath(root.left)
    right_path = longestPath(root.right)

    if len(left_path) > len(right_path):
        longest_root = left_path
    elif len(left_path) < len(right_path):
        longest_root = right_path
    else:
        # If both paths are of equal length, compare the node values of their first elements
        # Choose the path with the node value closer to the root
        if root.left and root.right:
            if left_path[0] < right_path[0]:
                longest_root = left_path
            else:
                longest_root = right_path
        elif root.left:
            longest_root = left_path
        else:
            longest_root = right_path

    longest_root.append(root.data)
    return longest_root

    

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
path = longestPath(root)
for ele in path:
    print(ele)