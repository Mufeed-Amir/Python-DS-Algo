class ListNode:
     def __init__(self,val,next=None):
          self.val=val
          self.next=None
class Stack:
     def __init__(self):
          self.head=None
          self.tail=None

     def __iter__(self):
          tempNode=self.head
          while tempNode:
               yield tempNode
               tempNode=tempNode.next

     def __str__(self):
          values=[str(x.val) for x in self]
          return "\n".join(values)

     def push(self,val):
          newNode=ListNode(val)
          newNode.next=self.head
          self.head=newNode

     def isEmpty(self):
          if self.head==None:
               return True
          else:
               return False

     def pop(self):
          if self.isEmpty():
               return -1
          else:
               self.head=self.head.next

     def peek(self):
          return self.head.val
     
     def size(self):
          tempNode=self.head
          count=0
          while tempNode:
               count +=1
               tempNode=tempNode.next
          return count

class MyQueue:
     def __init__(self):
          self.stack1=stack()
          self.stack2=stack()

     def push(self, x: int) -> None:

          
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        

    def peek(self) -> int:
        """
        Get the front element.
        """