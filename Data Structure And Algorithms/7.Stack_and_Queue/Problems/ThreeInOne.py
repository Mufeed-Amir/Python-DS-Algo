class MultiStack:

     def __init__(self,stackSize):
          self.numberOFstacks=3
          self.list=[None]*stackSize*3
          self.sizes=[0]*self.numberOFstacks
          self.stackSize= stackSize
     
     def __str__(self):
          values=[str(x) for x in self.list]
          return "-".join(values) 
     
     def isFull(self,stackNum):
          if self.sizes[stackNum-1]==self.stackSize:
               return True 
          else:
               return False
     def isEmpty(self,stackNum):
          if self.sizes[stackNum-1]==0:
               return True
          else: 
               return False
     def push(self,val,stackNum):

          if stackNum==1:
               if self.isFull(stackNum):
                    print(f"Stack {stackNum} Is FULL !")
               else:
                    self.list[self.sizes[stackNum-1]]=val
                    self.sizes[stackNum-1] += 1
          elif stackNum==2:
               if self.isFull(stackNum):
                    print(f"Stack {stackNum} Is FULL !")
               else:
                    self.list[self.sizes[stackNum-1] + int(self.stackSize/3) ]=val
                    self.sizes[stackNum-1]  += 1
          
          elif stackNum==3:
               if self.isFull(stackNum):
                    print(f"Stack {stackNum} Is FULL !")
               else:
                    self.list[self.sizes[stackNum-1] + int(2*self.stackSize/3) ]=val
                    self.sizes[stackNum-1]  += 1
          else:
               print("Enter valid stackNum")
     
     def pop(self,stackNum):

          if stackNum==1:
               if self.isEmpty(stackNum):
                    return "Stack is Empty"
               else:
                    k=self.list[self.sizes[stackNum-1]-1]
                    self.list[self.sizes[stackNum-1]-1]=None
                    self.sizes[stackNum-1] -=1
                    return k
          elif stackNum==2:
               if self.isEmpty(stackNum):
                    return "Stack is Empty"
               else:
                    k=self.list[self.sizes[stackNum-1] + int(self.stackSize/3)-1]
                    self.list[self.sizes[stackNum -1] + int(self.stackSize/3)-1]=None
                    self.sizes[stackNum-1] -=1
                    return k
          elif stackNum==3:
               if self.isEmpty(stackNum):
                    return "Stack is Empty"
               else:
                    k=self.list[self.sizes[stackNum-1] + 2*int(self.stackSize/3)-1]
                    self.list[self.sizes[stackNum-2] + 2*int(self.stackSize/3)-1]=None
                    self.sizes[stackNum-1] -=1
                    return k
          else:
               return "Enter a valid StackNum"

     def peek(self,stackNum):
          if stackNum==1:
               if self.isEmpty(stackNum):
                    return "Stack is Empty"
               else:
                    return self.list[self.sizes[stackNum-1]-1]
          elif stackNum==2:
               if self.isEmpty(stackNum):
                    return "Stack is Empty"
               else:
                    return self.list[self.sizes[stackNum-1] + int(self.stackSize/3)-1]
               
          elif stackNum==3:
               if self.isEmpty(stackNum):
                    return "Stack is Empty"
               else:
                    return self.list[self.sizes[stackNum-1] + 2*int(self.stackSize/3)-1]
               
          else:
               return "Enter a valid StackNum"
          



elisha=MultiStack(3)
elisha.push(8888, 1)
elisha.push(777, 1)
# print(elisha.pop(1))
elisha.push(7,2)
elisha.push(13,2)
elisha.push(13,2)
elisha.push(7,3)
elisha.push(13,3)
elisha.push(13,3)
print(elisha.peek(2))
print(elisha)
print(elisha.sizes)



