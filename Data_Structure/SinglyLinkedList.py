"""
A singly linked list is a data structure in computer science used for organizing and storing a collection of elements, called nodes.
Each node in a singly linked list contains two components data and next_addr

Singly linked list is efficient in insertion deletion compared to Arrays.
Accessing elements in SLL is slower compared to arrays, as it need to traverse the sequence elements from begining to access any given element.

"""
class Signly_linked_list:
    def __init__(self,data):
        self.data=data
        self.next_node_addr=None
    def set_data(self,new):
        self.data=new
    def get_data(self):
        return self.data
    def set_next_addr(self,node_addr):
        self.next_node_addr=node_addr
    def get_next_addr(self):
        return self.next_node_addr   
        
node1=Signly_linked_list(10)
node2=Signly_linked_list(20)
node3=Signly_linked_list(30)
node4=Signly_linked_list(40)

node1.set_next_addr(node2)  
node2.set_next_addr(node3) 
node3.set_next_addr(node4) 

print(node1.get_next_addr())
print(node2.get_next_addr())
print(node3.get_next_addr())


print(node1.get_data())
print(node2.get_data())
print(node3.get_data())
print(node4.get_data())
