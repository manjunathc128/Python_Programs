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
