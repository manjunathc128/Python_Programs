"""
Array : Array is a linear/structured data type used to store multiple values with reference to one variable.
Array store the data in contiguous memory allocation 
Time complexity :

Indexing/accessing  O(1)                 = base memory + (index * size of element)
Insertion/Deletion at begining O(n)      = because of copy operation
Insertion/Deletion at middle O(n)        = because of copy operation
Insertion?Deletion at end O(1)           = because of no copy operation
 

Two types of array 
1 Static array
2 Dyanmic array

static array : Static array is data structure which is used to store data elements in fix sized memory d

"""
 
class Static_Array:
    def __init__(self,size):
        self.size=size
        self.array=[]*self.size
        
    def index(self,ind):
        return self.array[ind]
        
    def show(self):
        return self.array
        
    def insert(self,data):
        self.array.append(data)
        
    def delet(self,index):
        self.array.pop(index)

a=Static_Array(5)  

a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)

print(a.show())       
print(a.index(3))     
        
