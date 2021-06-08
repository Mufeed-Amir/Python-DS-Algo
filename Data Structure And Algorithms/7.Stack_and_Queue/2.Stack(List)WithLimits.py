class Stack:
     def __init__(self,sizeMax):
          self.list=[]
          self.sizeMax=sizeMax

     def __str__(self):
          if self.list==[]:
               return "Stack is Empty"
          else:
               values=[str(x) for x in self.list]
               values.reverse()
               return "\n".join(values)
     def isEmpty(self):
          if self.list==[]:
               return True
          else:
               return False
     def isFull(self):
          if len(self.list)==self.sizeMax:
               return True
          else:
               False
     def push(self,val):
          if len(self.list)<self.sizeMax:
               self.list.append(val)
          else:
               print("__StackOverFlow__")
     def pop(self):
          if self.list==[]:
               return "Stack is Empty"
          else:
               return self.list.pop()
     def delete(self):
          self.list=[]
          return "Stack has been Emptied"


stack=Stack(5)
stack.push(1)     
stack.push(2)     
stack.push(3)     
stack.push(4)     
stack.push(5)     
stack.push(5)     
print(stack) 
stack.pop()
print("____________________")
print(stack)  