"""
general Tree : Tree is a non linear data structure made up nodes each node have zero or more child nodes 
 search for a node in nonstraightforward. 
It is a hierarchical data structure that consists of nodes connected by edges. 
Example : Directory file system, routing protocols, organization chart.
Some of the algoritms based on general tree traversal : Breath first search and Deapth first search

"""

class TreeNode:
    def __init__(self,data):
        self.data =data
        self.childern=[]
        self.parent=None
    def add_child(self,data):
        data.parent=self
        self.childern.append(data)
        
    def print_child(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.childern:
            for child in self.childern:
                child.print_child()
    
    def get_level(self):
        p=self.parent
        level=0
        
        while p:
            level += 1
            p=p.parent
        return level
        
Electronics=TreeNode("Electronics")



Laptop=TreeNode("Laptop")
Phone=TreeNode("Phone")
Tvs=TreeNode("Tvs")

Electronics.add_child(Laptop)
Electronics.add_child(Phone)
Electronics.add_child(Tvs)


Laptop.add_child(TreeNode("HP"))
Laptop.add_child(TreeNode("Dell"))
Laptop.add_child(TreeNode("Lenovo"))


Phone.add_child(TreeNode("Nokia"))
Phone.add_child(TreeNode("Samsung"))
Phone.add_child(TreeNode("oppo"))

Tvs.add_child(TreeNode("LG"))
Tvs.add_child(TreeNode("sony"))
Tvs.add_child(TreeNode("savy"))

Electronics.print_child()

print(Phone.get_level())
