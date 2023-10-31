""" 
    BinarySearchTreeNode makes use of Tree data structure organizes values it it.
    BinarySearchTreeNode doesnot allow duplicate values as a node in it (binary search will be sorted with sorted)
    BinarySearchTreeNode adds new node with respect to root node to the left if new node lesser than current node else to the right 
    BinarySearchTreeNode has three search traversal mechanism inorder, preorder, postorder
    BinarySearchTreeNode takes list of values to create BinaryTree and always first value in list is root node
    BinarySearchTreeNode search element/node in order of logn time complexity so every search starts from root node 
    
"""
class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def addChild(self,data):
        if self.data == data:
            return 
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left=BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right=BinarySearchTreeNode(data)
                
    def Binarysearch(self,val):
        if val == self.data:
            return True
        else:
            if val < self.data:
                if self.left:
                    return self.left.Binarysearch(val)
                else:
                    return False
            else:
                if self.right:
                    return self.right.Binarysearch(val)
                else:
                    return False
         
    def inOrderTraversal(self):
        datalist=[]
        
        if self.left:
            datalist += self.left.inOrderTraversal()
        
        datalist.append(self.data)
            
        if self.right:
            datalist += self.right.inOrderTraversal()
            
        return datalist
        
    def preorderTraversal(self):
        # datalist=[]
        # datalist.append(self.data)
        datalist=[self.data]
        if self.left:
            datalist+=self.left.preorderTraversal()
        if self.right:
            datalist+=self.right.preorderTraversal()
        return datalist   
        
    def postorderTraversal(self):
        datalist=[]
        if self.left:
            datalist+=self.left.preorderTraversal()
        if self.right:
            datalist+=self.right.preorderTraversal()
            
        datalist.append(self.data)    
        
        return datalist
    
    def findMin(self):
        if self.left :
            return self.left.findMin()
        return self.data
        
    def findMax(self):
        if self.right:
            return self.right.findMax()
        return self.data
        
def buildTree(arr):
    root = BinarySearchTreeNode(arr[0])
    for node in arr:
        root.addChild(node)
    return root
    
arr=[12,13,1,6,4,5,2,9,7,8,10,11]  
tree=buildTree(arr)

print(tree.inOrderTraversal())
print(tree.Binarysearch(3))
print(tree.findMin())
print(tree.findMax())
print(tree.preorderTraversal())
print(tree.postorderTraversal())



