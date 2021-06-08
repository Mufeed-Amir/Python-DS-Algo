class Stack:
     def __init__(self):
          self.list=[]
     
     def __str__(self):
          if self.list==[]:
               return "Stack is Empty"
          else:
               values=self.list.reverse()
               values=[str(x) for x in self.list]
               return "\n".join(values)
     
     def isEmpty(self):
          if self.list== []:
               return True
          else:
               return False

     def push(self,val):
          self.list.append(val)
          return "The element has been successfully inserted"
     
     def pop(self):
          if self.isEmpty():
               return "Stack is Empty"
          else:
               return self.list.pop()
     def peek(self):
          if self.isEmpty():
               return "Stack is Empty"
          else: 
               return self.list[-1]
     def delete(self):
          self.list=[]
          return ("Stack has been deleted successfully")
          


stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
print(stack.peek())
print(stack.delete())
print(stack)