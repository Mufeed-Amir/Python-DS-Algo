from QueueClass import *
class TreeNode:
     def __init__(self,val):
          self.val=val
          self.left=None
          self.right=None

rootNode=TreeNode(1)  
n2=TreeNode(2)
n3=TreeNode(3)
n4=TreeNode(4)
n5=TreeNode(5)
n6=TreeNode(6)
n7=TreeNode(7)
rootNode.left=n2
rootNode.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n3.right=n7

"""            n1
          n2        n3
     n4        n5     """

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
def preOrderTraversal(rootNode):
     if not rootNode:
          return
     else:
          print(rootNode.val)
          preOrderTraversal(rootNode.left)
          preOrderTraversal(rootNode.right)

def postOrderTraversal(rootNode):
     if not rootNode:
          return
     else:
          preOrderTraversal(rootNode.left)
          preOrderTraversal(rootNode.right)
          print(rootNode.val)
          
def inOrderTraversal(rootNode):
     if not rootNode:
          return
     else:
          preOrderTraversal(rootNode.left)
          print(rootNode.val)
          preOrderTraversal(rootNode.right)
def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Not found"

def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully Inserted"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully Inserted"
          

inOrderTraversal(rootNode)
     

                    



