from QueueClass import *
class TreeNode:
     def __init__(self,val):
          self.val=val
          self.leftchild=None
          self.rightchild=None

n1=TreeNode(1)  
n2=TreeNode(2)
n3=TreeNode(3)
n4=TreeNode(4)
n5=TreeNode(5)
n6=TreeNode(6)
n7=TreeNode(7)
n1.leftchild=n2
n1.rightchild=n3
n2.leftchild=n4
n2.leftchild=n5
n3.leftchild=n6
n4.rightchild=n7
"""            n1
          n2        n3
     n4        n5     """

def traversal(rootNode):
     if not rootNode:
          return
     else:
          q=Queue()
          q.enQueue(rootNode)
          tempNode=q.head
          while not q.isMT():
               val=q.deQueue()
               print(val.val)
               if val.leftchild:
                    q.enQueue(val.leftchild)
               if val.rightchild:
                    q.enQueue(val.rightchild)

traversal(n1)
     

                    



