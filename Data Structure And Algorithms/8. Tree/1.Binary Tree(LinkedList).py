class TreeNode:
     def __init__(self,val):
          self.val=val
          self.leftChild=None
          self.rightChild=None

tree=TreeNode(1)
two=TreeNode(2)
three=TreeNode(3)
four=TreeNode(4)
five=TreeNode(5)
six=TreeNode(6)
seven=TreeNode(7)
tree.leftChild=two
tree.rightChild=three
two.leftChild=four
two.rightChild=five
three.leftChild=six
three.rightChild=seven


def preOrderTraversal(rootNode):
     if not rootNode:
          return
     print(rootNode.val)
     preOrderTraversal(rootNode.leftChild)
     preOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
     if not rootNode:
          return
     postOrderTraversal(rootNode.leftChild)
     postOrderTraversal(rootNode.rightChild)
     print(rootNode.val)

def inOrderTraversal(rootNode):
     if not rootNode:
          return 
     inOrderTraversal(rootNode.leftChild)
     print(rootNode.val)
     inOrderTraversal(rootNode.rightChild)

from QueueClass import *

def levelOrderTraversal(rootNode):
     if not rootNode:
          return
     else:
          customQueue=Queue()
          customQueue.enQueue(rootNode)
          while not(customQueue.isEmpty()):
               root=customQueue.deQueue()
               print(root.val)
               if root.leftChild !=None:
                    customQueue.enQueue(root.leftChild)
               if root.rightChild != None:
                    customQueue.enQueue(root.rightChild)
          
def searchNode(rootNode,val):

     if not rootNode:
          return
     else:
          queue=Queue()    
          queue.enQueue(rootNode)
          while not queue.isEmpty():
               rt=queue.deQueue()
               if rt.val==val:
                    return "Found"
               if rt.leftChild !=None:
                    queue.enQueue(rt.leftChild)
               if rt.rightChild !=None:
                    queue.enQueue(rt.rightChild)

     return "Not Found"

def insertNode(rootNode,nodeVal):
     newNode=TreeNode(nodeVal)
     if not rootNode:
          rootNode.leftChild=newNode
     else:
          queue=Queue()
          queue.enQueue(rootNode)
          while  not(queue.isEmpty()):
               rt=queue.deQueue()
               if rt.leftChild==None:
                    rt.leftChild=newNode
                    return
               elif rt.leftChild !=None and rt.rightChild ==None:
                    rt.rightChild=newNode
                    return

               if rt.leftChild !=None:
                    queue.enQueue(rt.leftChild)
               if rt.rightChild !=None:
                    queue.enQueue(rt.rightChild)
          
insertNode(tree, 8)
insertNode(tree, 9)
insertNode(tree, 10)
insertNode(tree, 11)
# levelOrderTraversal(tree)
levelOrderTraversal(tree)







