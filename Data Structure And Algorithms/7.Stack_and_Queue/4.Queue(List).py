class Queue:
     def __init__(self):
          self.list=[]

     def __str__(self):
          item=[str(i) for i in self.list]
          return " ".join(item)
     def isEmpty(self):
          if self.list==[]:
               return True
          else:
               return False
     def enqueue(self,value):
          self.list.append(value)

     def dequeue(self):
          if self.isEmpty():
               return "Queue is Empty"
          else:
               return self.list.pop(0)
     
     def peek(self):
          return self.list[0]
     
     def delete(self):
          self.list=[]
          return "Queue is successfully deleted!"


queue=Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue)
print(queue.isEmpty())
print("----------->>>",queue.dequeue())
print(queue)

