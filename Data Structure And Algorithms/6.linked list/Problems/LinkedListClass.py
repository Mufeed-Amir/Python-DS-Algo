from typing import *
from random import randint
class ListNode:
     def __init__(self,value=None):
          self.value=value
          self.next=None
          self.prev=None
     def __str__(self):
          return str(self.value)

class LinkedList:
     def __init__(self):
          self.head=None
          self.tail=None

     def __iter__(self):
          curNode=self.head
          while curNode:
               yield curNode
               curNode=curNode.next
     def __str__(self):
          values=[str(x.value) for x in self]
          return " --> ".join(values)
     
     def __len__(self):
          result=0
          node=self.head
          while node:
               result +=1
               node=node.next
          return result
     def add(self,value):
          newNode=ListNode(value)
          if self.head==None:
               self.head=newNode
               self.tail=newNode
          else:
               self.tail.next=newNode
               self.tail=newNode

     def generator(self,n,min_value,max_value):
          self.head=None
          self.tail=None
          for i in range(n):
               self.add(randint(min_value,max_value))
          return self

     def RemoveNumber(self,num):
          tempNode=self.head
          while tempNode.next:
               if tempNode.next.value==num:
                    tempNode.next=tempNode.next.next   
               else:
                    tempNode=tempNode.next
          if self.head.value==num:
               self.head=self.head.next
     def RemoveDuplicate(self):
          tempNode=self.head
          a={tempNode.value,}
          while tempNode.next:
               if tempNode.next.value in a:
                    tempNode.next=tempNode.next.next
               else:
                    a.add(tempNode.next.value)
                    tempNode=tempNode.next
               
if __name__=="__main__":
     linkedlist=LinkedList()
     linkedlist.add(1)
     linkedlist.add(1)
     linkedlist.add(1)
     linkedlist.add(3)
     linkedlist.add(3)
     linkedlist.add(4)
     linkedlist.add(5)
     linkedlist.add(6)
     linkedlist.add(6)
     linkedlist.add(6)
     linkedlist.add(7)
     linkedlist.add(7)
     linkedlist.RemoveDuplicate()
     print(linkedlist)


