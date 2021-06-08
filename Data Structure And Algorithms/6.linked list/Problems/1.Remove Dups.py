from LinkedListClass import *

def RemoveDuplicate(link):
     tempNode=link.head
     a=set([tempNode.value])
     while tempNode.next:
          if tempNode.next.value in a:
               tempNode.next=tempNode.next.next
          else:
               a.add(tempNode.next.value)
               tempNode=tempNode.next     
     return link

link=LinkedList()
link.generator(5,0,5)
print(link)
RemoveDuplicate(link)
print(link)