from LinkedListClass import *
def Partition(linkedlist,x):
     head=linkedlist.head
     if head==None:
       return head
     travNode=head
     head1=ListNode(0)
     tail1=head1
     head2=ListNode(0)
     tail2=head2
     while travNode:
          if travNode.value<x:
               tail1.next=ListNode(travNode.value)
               tail1=tail1.next
          else:
               tail2.next=ListNode(travNode.value)
               tail2=tail2.next
                
          travNode=travNode.next            
     tail1.next=head2.next
     tail1=head2=None
     linkedlist.head=head1.next
     head1=None
     return head

linkedlist=LinkedList()
linkedlist.generator(7,0 , 9)
print(linkedlist)
Partition(linkedlist, 3)
print(linkedlist)