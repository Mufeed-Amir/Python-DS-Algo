from LinkedListClass import *

def ReverseLinkedList(linkedlist):
     head=linkedlist.head
     if head==None or head.next==None:
          return head
     prevNode=head
     curNode=prevNode.next
     prevNode.next=None
     while curNode:
          nextNode=curNode.next
          curNode.next=prevNode
          prevNode=curNode
          curNode=nextNode
     
     linkedlist.head=prevNode

linkedlist=LinkedList()
linkedlist.generator(5,0 ,100)
print(linkedlist)
ReverseLinkedList(linkedlist)
print(linkedlist)

