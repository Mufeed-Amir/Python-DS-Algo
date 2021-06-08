class ListNode:
     def __init__(self,data=None):
          self.data=data
          self.next=None

class CircularSinglyLinkedList:
     def __init__(self):
          self.head=None
          self.tail=None

     def traverseLinkedList(self):
          a=[]
          tempNode=self.head
          while tempNode!=None:
               a.append(tempNode.data)
               if tempNode.next==self.head:
                    break
               tempNode=tempNode.next
          return a
               
     def insertLinkedList(self,location,value):
          newNode=ListNode(value)
          if self.head==None:
               return "Circular_Singly_Linked_List doesn't exits"
          else:
               if location==0:
                    newNode.next=self.head
                    self.head=newNode
                    self.tail.next=newNode
               elif location==-1:
                    self.tail.next=newNode
                    self.tail=newNode
                    newNode.next=self.head
               else:
                    tempNode=self.head
                    i=0
                    while i<location-1:
                         tempNode=tempNode.next
                         i +=1
                    
                    nextNode=tempNode.next
                    newNode.next=nextNode
                    tempNode.next=newNode

     def deleteNode(self,location):
          if self.head==None:
               return "LinkedList doesn't exists!"
          elif self.tail==self.head:
               self.head.next=None
               self.head=None
               self.tail=None
          
          else:
               if location==0:
                    self.tail.next=self.head.next
                    self.head=self.head.next
               elif location==-1:
                    tempNode=self.head
                    while tempNode!=None:
                         tempNode=tempNode.next
                         if tempNode.next==self.tail:
                              break
                    tempNode.next=self.head
                    self.tail=tempNode
               else:
                    tempNode=self.head
                    i=0
                    while i<location-1:
                         tempNode=tempNode.next
                         i=i+1
                    
                    tempNode.next=tempNode.next.next
     
     def deleteLinkedList(self):
          self.tail.next=None
          self.head=None
          self.tail=None
          return "Your Linked List is successfully deleted!!"









CSinglyLinkedList=CircularSinglyLinkedList()
first=Node(8)
second=Node(27)
third=Node(64)
CSinglyLinkedList.head=first
first.next=second
second.next=third
third.next=first
CSinglyLinkedList.tail=third
CSinglyLinkedList.insertLinkedList(0,100)
CSinglyLinkedList.insertLinkedList(1,99)
CSinglyLinkedList.insertLinkedList(2,98)
CSinglyLinkedList.insertLinkedList(3,97)
CSinglyLinkedList.insertLinkedList(-1,1000)
# CSinglyLinkedList.deleteNode(3)
# CSinglyLinkedList.deleteLinkedList()
print(CSinglyLinkedList.traverseLinkedList())

