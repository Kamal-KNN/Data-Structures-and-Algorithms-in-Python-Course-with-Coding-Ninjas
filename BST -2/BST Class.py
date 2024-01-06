class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    def printhelper(self,root):
        if root is None:
            return
        print(root.data,end=":")
        if root.left is not None:
            print("L:",end="")
            print(root.left.data,end=",")
        if root.right is not None:
            print("R:",end="")
            print(root.right.data,end="")
        print()
        self.printhelper(root.left)
        self.printhelper(root.right)
        
        
    
    
    def printTree(self):
        self.printhelper(self.root)
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
    def searchhelper(self,root,data):
        if root is None:
            return False
        if root.data==data:
            return True
        if data<root.data:
            return self.searchhelper(root.left,data)
        if data>root.data:
            return self.searchhelper(root.right,data)
        return False

    
    def search(self, data):
        return self.searchhelper(self.root,data)
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
    def inserthelper(self,root,data):
        if root is None:
            newnode=BinaryTreeNode(data)
            return newnode
        if data<=root.data:
            root.left=self.inserthelper(root.left,data)
        if data>root.data:
            root.right=self.inserthelper(root.right,data)
        return root

        
    def insert(self, data):
        self.numNodes+=1
        self.root=self.inserthelper(self.root,data)
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
    def min(self,root):
        if root is None:
            return 1000
        if root.left is None:
            return root.data
        return self.min(root.left)
    def deletedhelper(self,root,data):
        if root is None:
            return False,None
        if root.data==data:
            if root.left is None and root.right is None:                    #In-case of leaf node
                del root
                return True,None
            elif root.left is not None and root.right is None:           #In-case of left node
                temp=root.left
                del root
                return True,temp
            elif root.left is None and root.right is not None:
                temp=root.right
                del root
                return True,temp
            else:
                rightmin=self.min(root.right)
                root.data=rightmin
                deleted,root.right=self.deletedhelper(root.right,rightmin)
                return deleted,root


        if data<root.data:
            deleted,newroot=self.deletedhelper(root.left,data)
            root.left=newroot
        if data>root.data:
            deleted,newroot=self.deletedhelper(root.right,data)
            root.right=newroot
        return deleted,root
      
    def delete(self, data):
        deleted,newroot=self.deletedhelper(self.root,data)
        if deleted:
            self.numNodes-=1
        self.root=newroot
        return deleted
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
    
    def count(self):
        return self.numNodes
        
b = BST()
q = int(input())
while (q > 0) :
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q-=1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
        b.printTree()