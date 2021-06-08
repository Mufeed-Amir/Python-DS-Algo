class StackNode:
     def __init__(self,val):
          self.val=val
          self.next=None

class Stack:
     def __init__(self):
          self.head=None
     
     def __iter__(self):
          tempNode=self.head
          while tempNode:
               yield tempNode
               tempNode=tempNode.next
     def __str__(self):
          array=[str(x.val) for x in self]
          return "\n--\n".join(array)

     def push(self,value):
          newNode=StackNode(value)
          newNode.next=self.head
          self.head=newNode

     def pop(self):
          if self.head==None:
               return "Stack is Empty"
          else:
               k=self.head.val
               self.head=self.head.next
               return k

     def isEmpty(self):
          if self.head==None:
               return True
          else:
               return False

     def peek(self):
          return self.head.val
     def delete(self):
          self.head=None
          return "Stack is successfully deleted!!"

stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack)
print("Element: ",stack.pop())
print(stack)
print(stack.peek())
print(stack.isEmpty())
saaaaaaaaaaaaazq                                  