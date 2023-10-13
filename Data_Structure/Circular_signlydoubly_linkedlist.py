














class Circular_Doubly_linked_list:
    def __init__(self,data):
        self.data=data
        self.next_node_addr=None
        self.prev_node_addr=None
    def set_data(self,new):
        self.data=new
        
    def get_data(self):
        return self.data
        
    def set_next_addr(self,node_addr):
        self.next_node_addr=node_addr
        
    def get_next_addr(self):
        return self.next_node_addr   
        
    def set_prev_addr(self,node_addr):
        self.prev_node_addr=node_addr
        
    def get_prev_addr(self):
        return self.prev_node_addr    
        
node1=Doubly_linked_list(10)
node2=Doubly_linked_list(20)
node3=Doubly_linked_list(30)
node4=Doubly_linked_list(40)

node1.set_next_addr(node2)  
node2.set_next_addr(node3) 
node3.set_next_addr(node4) 

# last node stores address of first node
node4.set_next_addr(node1)
# first node stores address of last node
node1.set_prev_addr(node4)

node2.set_prev_addr(node1) 
node3.set_prev_addr(node2) 
node4.set_prev_addr(node3)

print(node1.get_next_addr())
print(node2.get_next_addr())
print(node3.get_next_addr())


print(node1.get_prev_addr())
print(node2.get_prev_addr())
print(node3.get_prev_addr())


print(node1.get_data())
print(node2.get_data())
print(node3.get_data())
print(node4.get_data())
