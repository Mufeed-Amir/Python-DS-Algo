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
          
          k=self.head.val
          self.head=self.head.next
          return k

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
          self.stack1=Stack()
          self.stack2=Stack()

     def push(self, x: int) -> None:
          self.stack1.push(x)
          return None
     def pop(self) -> int:
          tempNode=self.stack1.head
          while tempNode:
               self.stack2.push(self.stack1.pop())
               tempNode=tempNode.next
          
          ret=self.stack2.pop()
          tempNode=self.stack2.head
          while tempNode:
               self.stack1.push(self.stack2.pop())
               tempNode=tempNode.next
          
          return ret

     def peek(self) -> int:
          tempNode=self.stack1.head
          while tempNode.next:
               tempNode=tempNode.next
          
          return tempNode.val

elishaQ=MyQueue()
elishaQ.push(1)
elishaQ.push(2)
elishaQ.push(3)
elishaQ.push(4)
elishaQ.push(5)
elishaQ.pop()
print(elishaQ.peek())