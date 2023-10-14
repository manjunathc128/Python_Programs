'''
Stack: Stack is temprorary memory that stores the data in the linear and first in last out passsion 
stack works on the principle of FILO, LIFO
Stack has only one end elements can be accessed only in one direction.

once stack is initiated with specific size and memory is allocated accordingly, the size is fixed and cannot be changed in lifetime.

if we need a stack with desired size we have to copy the elements from old stack amd place it into new stack

''' 


class Stack:
  def __init__(self,size):
    self.l=[]
    self.size=size
  def show(self):
      return self.l
  def push(self,data):
    if len(self.l) == self.size:
      raise ValueError('stack is full')
    else: 
      self.l.append(data)
  def pop(self):
    if len(self.l) == 0:
      raise ValueError('stack is empty')
    else:
      self.l.pop()
      
s1=Stack(5)   
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
print(s1.show())
