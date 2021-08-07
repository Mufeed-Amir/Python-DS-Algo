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
     def preOrderTraversal(self):
          pass

                    
alisha=TreeNode(8)
alisha.insertNode(1)
alisha.insertNode(2)
alisha.insertNode(3)
alisha.insertNode(4)
alisha.insertNode(5)
alisha.insertNode(6)
alisha.insertNode(7)
print(alisha.searchNode(2))