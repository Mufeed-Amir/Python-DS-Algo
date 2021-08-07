class TreeNode:
     def __init__(self,size):
          self.list=[None]*size
          self.sizeMax=size
          self.lastUI=0

     def insertNode(self,val):
          if self.lastUI + 1 ==self.sizeMax:
               return
          
          self.list[self.lastUI+1]=val
          self.lastUI +=1
     def searchNode(self,target):
          for val in self.list:
               if val==target:
                    return 1
          return -1
     def preOrderTraversal(self,index):
          if index > self.lastUI:
               return
          else:
               print(self.list[index])
               self.preOrderTraversal(2*index)
               self.preOrderTraversal(2*index+1)
     def postOrderTraversal(self,index):
          if index > self.lastUI:
               return
          else:
               self.preOrderTraversal(2*index)
               self.preOrderTraversal(2*index+1)
               print(self.list[index])
     def inOrderTraversal(self,index):
          if index > self.lastUI:
               return
          else:
               self.preOrderTraversal(2*index)
               print(self.list[index])
               self.preOrderTraversal(2*index+1)
     def levelOrderTraversal(self):
          for i in range(1,len(self.list)):
               print(self.list[i])

                    
alisha=TreeNode(8)
alisha.insertNode(1)
alisha.insertNode(2)
alisha.insertNode(3)
alisha.insertNode(4)
alisha.insertNode(5)
alisha.insertNode(6)
alisha.insertNode(7)
# print(alisha.searchNode(2))
alisha.levelOrderTraversal()