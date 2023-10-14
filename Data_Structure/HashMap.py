"""
HashMap or HashTable: Hash map is a non linear data structure which stores the data based on hash code, non sequential 
manner . 

hashmap performs hash function on key and stores the value at index returned by hash function.

Time complexity : O(1) Insertion/deletion/accessing

"""

class HashMap:
    def __init__(self):
        self.Max=int(input("Enter the size of HashMap "))
        self.table=[None]*self.Max
        
    def get_hash(self,key):
        hash=0
        for char in key:
            hash += ord(char)
        return hash % self.Max
        
    def add_item(self,key,value):
        h=self.get_hash(key)
        self.table[h] = value
       
        
    def del_item(self, key):
        h = self.get_hash(key)
        self.arr[h] = None  
    
    def get_item(self,key):
        h=self.get_hash(key)
        return self.table[h]
        
hashmap1=HashMap()  
hashmap1.add_item("manju",5)
print(hashmap1.get_item("manju"))

