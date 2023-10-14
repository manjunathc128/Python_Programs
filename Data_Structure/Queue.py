"""

Queue: Queue is temprovary memory used to store the data in linear and  First in first out passion .
Queue works on the principle of FIFO, LILO.
the process of adding elements to queue is called as Enqueue operation.
the process of removing elements from queue is called as Dequeue operation.

once Queue is initiated with specific size and memory is allocated accordingly, the size is fixed and cannot be changed in lifetime.

if we need to modify a  Queue with desired size we have to copy the elements from old Queue amd place it into new queue
"""

class Queue:
    def __init__(self,size):
        self.l=[]
        self.size=size
    def Enqueue(self,data):
        if len(self.l) == self.size:
            raise ValueError('Queue is full')
        self.l.append(data)
        
    def Dequeue(self,index):
        if len(self.l) == 0:
            raise ValueError('Queue is Empty')
        self.l.pop(index)
        
    def showQueue(self):
        return self.l
Queue1=Queue(5)  

Queue1.Enqueue(1)
Queue1.Enqueue(2)
Queue1.Enqueue(3)
Queue1.Enqueue(4)
Queue1.Enqueue(5)

print(Queue1.showQueue())
