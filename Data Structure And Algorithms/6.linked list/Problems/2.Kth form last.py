from LinkedListClass import *

def KthFromLast(linkedlist,k):
     p1=linkedlist.head
     
     p2=linkedlist.head
     i=0
     while i<k:
          p2=p2.next
          i+=1
     
     while p2:
          p1=p1.next
          p2=p2.next

     return p1


linkedlist=LinkedList()
linkedlist.generator(7, 0, 10)
print(linkedlist)
print(KthFromLast(linkedlist, 3))