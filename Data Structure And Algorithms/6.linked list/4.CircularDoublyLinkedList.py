class Node:
     def __init__(self,data=None):
          self.data=data
          self.next=None
          self.prev=None

class DoublyCircular:
     def __init__(self):
          self.head=None
          self.tail=None
     
     def Ftraverse(self):
          tempNode=self.head
          a=[]
          while tempNode:
               a.append(tempNode.data)
               if tempNode.next==self.head:
                    break
               tempNode=tempNode.next
          return a

     def Rtraverse(self):
          tempNode=self.tail
          a=[]
          while tempNode!=None:
               a.append(tempNode.data)
               if tempNode==self.head:
                    break
               tempNode=tempNode.prev
          return a
     
     def Search(self,val):
          tempNode=self.tail
          while tempNode!=None:
               if tempNode==self.head:
                    break
               elif tempNode.data==val:
                    return "Congratulations!! You found it" 
               tempNode=tempNode.prev    
          return "I am Sorry!"

     def insert(self,location,value):
          newNode=Node(value)
          if self.head==None:
               self.head=newNode
               self.tail=newNode
               newNode.next=newNode
               newNode.prev=newNode
               
          else:
               if location==0:
                    newNode.next=self.head
                    self.head.prev=newNode
                    self.head=newNode
                    self.tail.next=newNode
                    newNode.prev=self.tail
               elif location==-1:
                    self.tail.next=newNode
                    newNode.prev=self.tail
                    newNode.next=self.head
                    self.tail=newNode
                    self.head.prev=newNode
               else:
                    tempNode=self.head
                    i=0
                    while i<location-1:
                         tempNode=tempNode.next
                         i +=1
                    nextNode=tempNode.next
                    newNode.next=nextNode
                    tempNode.next=newNode
                    nextNode.prev=newNode
                    newNode.prev=tempNode

     def deleteNode(self,location):
          if self.head==None:
               return "LinkedList doesn't exists!"
          elif self.head==self.tail:
               self.head.next=None
               self.head=None
               self.tail=None
          else:
               if location==0:
                    self.head=self.head.next
                    self.head.prev=None
                    self.tail.next=self.head
               elif location==-1:
                    tempNode=self.head
                    while tempNode:
                         if tempNode.next==self.tail:
                              break
                         tempNode=tempNode.next
                    nextNode=tempNode.next
                    nextNode.prev=None
                    tempNode.next=self.head
                    self.tail=tempNode
               else:
                    tempNode=self.head
                    i=0
                    while i<location-1:
                         tempNode=tempNode.next
                         i +=1
                    nextNode=tempNode.next
                    tempNode.next=nextNode.next
                    nextNode.next.prev=tempNode
                    nextNode.prev=None
          
     def deleteLinkedList(self):
          tempNode=self.head
          self.tail.next=None
          self.head.prev=None
          while self.head!=self.tail:
               self.head=self.head.next
               self.head.prev=None

          self.head=None
          self.tail=None

     
DCLinkedList=DoublyCircular()
first=Node(3)
second=Node(5)
third=Node(7)
DCLinkedList.head=first
first.next=second
second.prev=first
second.next=third
third.prev=second
third.next=first
DCLinkedList.tail=third
first.prev=DCLinkedList.tail
DCLinkedList.insert(0, 30)
DCLinkedList.insert(-1, 1729)
DCLinkedList.insert(4, 1752)
DCLinkedList.deleteLinkedList()
print(DCLinkedList.Ftraverse())
print(DCLinkedList.Rtraverse())
print(DCLinkedList.Search(5))
