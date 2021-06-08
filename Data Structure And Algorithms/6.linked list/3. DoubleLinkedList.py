class Node:
     def __init__(self,data=None):
          self.data=data
          self.next=None
          self.prev=None

class DoubleLinkedList:
     def __init__(self):
          self.head=None
          self.tail=None
     def RtraverseDLinkedList(self):
          a=[]
          tempNode=self.tail
          while tempNode!=None:
               a.append(tempNode.data)
               tempNode=tempNode.prev
               
          return a
     def FtraverseDLinkedList(self):
          a=[]
          tempNode=self.head
          while tempNode!=None:
               a.append(tempNode.data)
               tempNode=tempNode.next
               
          return a
     def insertDLinkedList(self,location,value):
          newNode=Node(value)
          if self.head==self.tail:
               newNode.prev=self.head
               self.head.next=newNode
               self.tail=newNode
          else:
               if location==0:
                    newNode.next=self.head
                    self.head.prev=newNode
                    self.head=newNode
               elif location==-1:
                    self.tail.next=newNode
                    newNode.prev=self.tail
                    self.tail=newNode
               else:
                    tempNode=self.head
                    i=0
                    while i<location -1 :
                         tempNode=tempNode.next
                         i +=1
                    nextNode=tempNode.next
                    newNode.next=nextNode
                    tempNode.next=newNode
                    newNode.prev=tempNode
                    nextNode.prev=newNode
     def deleteNodeDLinkedList(self,location):
          if self.head==self.tail:
               self.tail=None
               self.head=None
          elif self.head==None:
               return "Your DoublyLinkedList doesn't exits!!"
          else:
               if location==0:
                    self.head=self.head.next
                    self.head.prev=None 
               elif location==-1:
                    tempNode=self.head
                    while tempNode!=None:
                         if tempNode.next==self.tail: 
                              break
                         tempNode=tempNode.next
                    
                    self.tail.prev=None
                    self.tail=tempNode
                    tempNode.next=None
               else:
                    tempNode=self.head
                    i=0
                    while i<location-1:
                         tempNode=tempNode.next
                         i=i+1
                    nextNode=tempNode.next
                    tempNode.next=nextNode.next
                    nextNode.next.prev=tempNode
                    nextNode.prev=None
     
     def searchDLinkedList(self,val):
          tempNode=self.head
          while tempNode:
               if tempNode.data==val:
                    return True
               tempNode=tempNode.next
          return False
     def delteDLinkedList(self):
          if self.tail==self.head:
               self.tail=None
               self.head=None
          else:
               while self.tail!=self.head:
                    self.head=self.head.next
                    self.head.prev=None
                    
               self.head=None
               self.tail=None

          return "Your DLinkedList is successfully Deleted!!"

                 
dLinkedList=DoubleLinkedList()
first=Node(10)
second=Node(100)
third=Node(1000)
dLinkedList.head=first
first.next=second
second.prev=first
second.next=third
third.prev=second
dLinkedList.tail=third
dLinkedList.insertDLinkedList(0,2)
dLinkedList.insertDLinkedList(0,3)
dLinkedList.insertDLinkedList(0,4)
dLinkedList.insertDLinkedList(-1,4)
dLinkedList.insertDLinkedList(0,99)
dLinkedList.insertDLinkedList(1,53)
dLinkedList.insertDLinkedList(4,17)
print(dLinkedList.searchDLinkedList(53))
print(dLinkedList.FtraverseDLinkedList())
dLinkedList.deleteNodeDLinkedList(2)
dLinkedList.delteDLinkedList()
print(dLinkedList.RtraverseDLinkedList())
print(dLinkedList.FtraverseDLinkedList())