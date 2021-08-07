from QueueClass import *
class BSTNode:
     def __init__(self,val):
          self.val=val
          self.left=None
          self.right=None


def insertNode(rootNode,value):
     if rootNode.val==None:
          rootNode.val=value
     elif rootNode.val >= value:
          if rootNode.left==None:
               rootNode.left=BSTNode(value)
          else:
               insertNode(rootNode.left , value)   
     else:
          if rootNode.right==None:
               rootNode.right=BSTNode(value)
          else:
               insertNode(rootNode.right, value)
def levelOrderTraversal(rootNode):
     if not rootNode:
          return
     else:
          q=Queue()
          q.enQueue(rootNode)
          while not q.isMT():
               node=q.deQueue()
               print(node.val)
               if node.left:
                    q.enQueue(node.left)
               if node.right:
                    q.enQueue(node.right)

def inOrderTraversal(rootNode):
     if not rootNode:
          return
     else:
          inOrderTraversal(rootNode.left)
          print(rootNode.val)
          inOrderTraversal(rootNode.right)

def searchNode(rootNode,target):
     if not rootNode:
          return
     elif rootNode.val>=target:
          if rootNode.val==target:
               ret="Found"
               return ret
          else:
               ret=searchNode(rootNode.left, target)
     else:
          if rootNode.val==target:
               ret="found"
               return ret
          else:
               ret=searchNode(rootNode.right, target)
     return ret
def search(rootNode,target):
     if rootNode.val==target:
          print("Found")
     elif rootNode.val>target:
          if rootNode.left.val==target:
               print("Found")
          else:
               search(rootNode.left,target)
     else:
          if rootNode.right.val==target:
               print("Found")
          else:
               search(rootNode.right, target)    

           



rootNode=BSTNode(70)
insertNode(rootNode, 50)
insertNode(rootNode, 90)
insertNode(rootNode, 30)
insertNode(rootNode, 60)
insertNode(rootNode, 80)
insertNode(rootNode, 100)
insertNode(rootNode, 20)
insertNode(rootNode, 40)
insertNode(rootNode, 10)

inOrderTraversal(rootNode)
print(searchNode(rootNode, 10))
search(rootNode, 10)

