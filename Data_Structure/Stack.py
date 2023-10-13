class Stack:
  def __init__(self,size):
    self.l=[]
    self.size=size
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
