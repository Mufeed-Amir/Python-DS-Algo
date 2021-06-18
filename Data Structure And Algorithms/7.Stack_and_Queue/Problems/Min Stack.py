from typing import *
class StackNode:
     def __init__(self,val):
          self.val=val
          self.next=None
class MinStack:
     def __init__(self):

          self.head=None
          self.minVal=None

     def __iter__(self):
          tempNode=self.head
          while tempNode:
               yield tempNode
               tempNode=tempNode.next
     def __str__(self):
          values=[str(x.val) for x in self]
          return "  ".join(values) 

     def push(self, val: int) -> None:
          if self.head==None:
               self.minVal=val
               self.head=StackNode(self.minVal)
          else:
               if self.head.val > val:
                    self.minVal=val
                
               newNode=StackNode(self.minVal)
               newNode.next=self.head
               self.head=newNode
            
            
     def pop(self) -> None:
          self.head=self.head.next
        
     def top(self) -> int:
          return self.head.val
        
     def getMin(self) -> int:
          return self.head.val


elisha=MinStack()
elisha.push(1)
elisha.push(2)
elisha.push(3)
elisha.push(4)
print(elisha.getMin())
print(elisha)