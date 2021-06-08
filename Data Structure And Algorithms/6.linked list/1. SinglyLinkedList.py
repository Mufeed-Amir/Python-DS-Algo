class Node:
     def __init__(self,data):
          self.data=data
          self.next=None

class SinglyLinkedList:
     def __init__(self):
          self.head=None
          self.tail=None

     def insertLinkedList(self,location ,value):
          newNode=Node(value)
          if location==0:
               if self.head==None:
                    self.head=newNode
                    self.tail=newNode
               else:
                    newNode.next=self.head
                    self.head=newNode
          elif location==-1:
               if self.head==None:
                    self.head=newNode
                    self.tail=newNode
               else:
                    newNode.next=None
                    self.tail.next=newNode
                    self.tail=newNode
          else:
               tempNode=self.head
               i=0
               while i<location-1:
                    tempNode=tempNode.next
                    i=i+1

               nextNode=tempNode.next
               newNode.next=nextNode
               tempNode.next=newNode
          
     def traverseLinkedList(self):
          a=[]
          tempNode=self.head
          while tempNode != None:
               a.append(tempNode.data)
               tempNode=tempNode.next
          return a
     
     def searchingLinkedList(self,x):
          tempNode=self.head
          while tempNode!=None:
               if tempNode.data==x:
                    return True
               tempNode=tempNode.next
          return False
     def deleteNode(self,location):
          if self.head==None:
               return ("Singly_Linked_List doesn't exists!")
          else:
               if self.head==self.tail:
                    self.head=None
                    self.tail=None
               elif location==0:
                    self.head=self.head.next
               elif location==-1:
                    tempNode=self.head
                    while tempNode!=None:
                         if tempNode.next==self.tail:
                              break
                         tempNode=tempNode.next
                    
                    tempNode.next=None
                    self.tail=tempNode
               else:
                    tempNode=self.head
                    index=0
                    while index<location -1:
                         tempNode=tempNode.next
                         index=index + 1

                    nextNode=tempNode.next
                    tempNode.next=nextNode.next
     def deleteLinkedList(self):
          self.head=None
          self.tail=None
          return "Your Linked_List is successfully deleted!!"
                    

Slinkedlist=SinglyLinkedList()
first=Node(1)
second=Node(4)
third=Node(9)
Slinkedlist.head=first
first.next=second
second.next=third
Slinkedlist.tail=third
Slinkedlist.insertLinkedList(0, 100)
Slinkedlist.insertLinkedList(1, 99)
Slinkedlist.insertLinkedList(2, 98)
Slinkedlist.insertLinkedList(3, 97)
Slinkedlist.insertLinkedList(4, 96)
# print(Slinkedlist.deleteNode(0))
print(Slinkedlist.deleteLinkedList())

print(Slinkedlist.traverseLinkedList())
print(Slinkedlist.searchingLinkedList(9))



