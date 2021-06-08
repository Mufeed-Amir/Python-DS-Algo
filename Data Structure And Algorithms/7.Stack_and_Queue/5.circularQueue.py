class CircularQueue:
     def __init__(self,sizeMax):
          self.list=sizeMax*[None]
          self.sizeMax=sizeMax
          self.start=-1
          self.top=-1

     def __str__(self):
          items=[str(x) for x in self.list]
          return " <-- ".join(items)
     
     def isFull(self):
          if self.top + 1==self.start:
               return True
          elif self.start==0 and self.top+1==self.maxSize:
               return True
          else:
               return False

     def isEmpty(self):
          if self.top==-1:
               return True
          else: 
               return False

     def enqueue(self,value):
          if self.isFull():
               return "Queue is Full"

          else: 
               if self.top==self.mazSize:
                    self.top=0
               else:
                    self.top +=1
                    if self.start==-1:
                         self.start=0
               self.list[self.top]=value

     def dequeue(self):
          if self.isEmpty():
               return "Queue is Empty"
          else:
               


               
     def delete(self):
          self.start=-1
          self.top=-1
          self.list=None

cqueue=CircularQueue(5)
cqueue.enqueue(1)
cqueue.enqueue(2)
cqueue.enqueue(3)
cqueue.enqueue(4)
print(cqueue)
print("Mufeed",cqueue.dequeue())
print(cqueue)
cqueue.enqueue(17290)
print(cqueue)


     