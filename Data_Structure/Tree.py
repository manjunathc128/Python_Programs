"""
Tree data structure : Tree is non-linear data structure which is made up nodes which are arranged in non linear passion.
"""

class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            
            if data > self.data :        
                if self.right == None:
                    self.right=node(data)
                else:
                    self.right.insert(data)
    def showtree(self):
        if self.left:
            print(self.left.data)
            self.left.showtree()
        if self.right:
            print(self.right.data)
            self.right.showtree()
            
root=node(1)
root.insert(2)
root.insert(0)
root.insert(3)
root.insert(4)
root.showtree()

# -----------------------------General Tree with TreeNode Class -----------------------
class TreeNode:
    def __init__(self,data):
         self.data = data
         self.childern=[]
         self.parent=None
    def addChild(self,child):
        child.parent=self
        self.childern.append(child)
        
    def get_level(self):
        level=0
        parent=self.parent
        
        while parent:
            level+=1
            parent=parent.parent
        return level    
            
    def printTree(self):
        
        spaces=" " * self.get_level() * 2
        prefix = "|--" if self.parent else ""
        print(spaces + prefix + self.data)
        if self.childern:
            for child in self.childern :
                child.printTree()
            
def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.addChild(TreeNode("Mac"))
    laptop.addChild(TreeNode("Surface"))
    laptop.addChild(TreeNode("Thinkpad"))
    cellphone = TreeNode("Cell Phone")
    cellphone.addChild(TreeNode("iPhone"))
    cellphone.addChild(TreeNode("Google Pixel"))
    cellphone.addChild(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.addChild(TreeNode("Samsung"))
    tv.addChild(TreeNode("LG"))

    root.addChild(laptop)
    root.addChild(cellphone)
    root.addChild(tv)

    root.printTree()        
if __name__ == '__main__':
    build_product_tree()
