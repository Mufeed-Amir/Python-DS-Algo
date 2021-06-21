class ListNode:
     def __init__(self,val=None,next=None):
          self.val=val
          self.next=None
class Queue:
     def __init__(self):
          self.head=None
          self.tail=None
     def __iter__(self):
          tempNode=self.head
          while tempNode:
               yield tempNode
               tempNode=tempNode.next
     def __str__(self):
          values=[str(x.val) for x in self]
          return " ".join(values)
     def enQueue(self,val):
          newNode=ListNode(val)
          if self.head==None:
               self.head=newNode
               self.tail=newNode
          else:
               self.tail.next=newNode
               self.tail=newNode
     def isEmpty(self):
          if self.head==None:
               return True
          else:
               return False
     def deQueue(self):
          if self.isEmpty():
               return -1
          else:     
               k=self.head.val
               self.head=self.head.next
               return k

class AnimalShelter:
     def __init__(self):
          self.catQ=Queue()
          self.dogQ=Queue()
          self.num=1
     def enQueueAnimal(self,val,num): ## 0 for dog, 1 for cat
          if val==0:
               for i in range(0,num):
                    self.dogQ.enQueue(self.num)
                    self.num =self.num + 1
          if val==1:
               for i in range(0,num):
                    self.catQ.enQueue(self.num)
                    self.num =self.num +1

     def deQueueAnimal(self,val):
          if val==0:
               return self.dogQ.deQueue()
          if val==1:
               return self.catQ.deQueue()
     def deQueueAny(self):
          if self.catQ.head.val<self.dogQ.head.val:
               return self.catQ.deQueue(),"cat"
          else:
               return self.dogQ.deQueue(),"Dog"


lucy=AnimalShelter()
lucy.enQueueAnimal(0,2)
lucy.enQueueAnimal(1,2)
lucy.enQueueAnimal(0,2)
lucy.enQueueAnimal(1,1)
print(lucy.deQueueAny())
print(lucy.deQueueAnimal(1))
print(lucy.deQueueAnimal(0))
print(lucy.deQueueAny())



               
               