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

---------------------------------------------SinglyLinkedList---------------------------------
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self,head=None):
        self.head=head
        
    # insertBegining doesnt perform general python append operation 
    # insertBegining always insert at index position 0
    def insertBegining(self,data):  
        node=Node(data,self.head)
        self.head=node
        
    # insertEnd check LinkedList is empty or not 
    # If empty insert Node at head
    # If not empty traverse to n-1 and update next of n-1 Node with new Node 
    def insertEnd(self,data):
        if self.head is None:
            node=Node(data,self.head)
            self.head=node
        itr=self.head
        while itr.next:
            itr=itr.next
        
        itr.next=Node(data,None)
        
        
    def printLinkedList(self):
        if self.head is None:
            print('Linked List is Empty')
            return 
        itr=self.head
        llstr=''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr= itr.next
        print(llstr)    
          
     
    def insertValues(self,data_list):
        self.head=None
        for item in data_list:
            self.insertEnd(item)
            
    def get_length(self):
        count=0
        if self.head == None:
            return 0
        itr=self.head
        while itr:   
            count+=1
            itr=itr.next
        return count
        
    def removeNode(self,index):
        if not self.head :
            raise Exception('LinkedList is Empty')
        if index<0 or index>self.get_length():
            raise Exception('index out of range')
        if index == 0:
            self.head = self.next
            
        itr=self.head
        count=0
        while itr.next:
            if count == index -1 :
                itr.next = itr.next.next
                #del itr
                break
            itr=itr.next    
            count+=1
    def insertValue(self,data,index):
        if index<0 or index>self.get_length():
            raise Exception('index out of range')
        
        if index == 0:
            self.insertBegining(data)
        
        itr=self.head
        count=0
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                #break
            count+=1
            itr=itr.next
            
    def updateValue(self,data,index):
        if index<0 or index>self.get_length():
            raise Exception('index out of range')
        if index == 0:
            self.insertBegining(data)
            
        count=0
        itr=self.head
        while itr:
            if count == index-1:
                node = itr.next
                node1=Node(data,node.next)
                itr.next = node1
            count +=1
            itr=itr.next
    
            
L1=LinkedList()            
L1.insertBegining(7)        
L1.insertBegining(6) 
L1.insertBegining(5) 

L2=LinkedList()
L2.insertValues(['bannana','apple','avacado','kiwi'])

print(L1.get_length())
print(L2.get_length())

# L1.removeNode(1)

L1.printLinkedList()
L1.insertValue(0,1)
L1.printLinkedList()
L1.updateValue(4,1)
L1.printLinkedList()

L2.printLinkedList()

