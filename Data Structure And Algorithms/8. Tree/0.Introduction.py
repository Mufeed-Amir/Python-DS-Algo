class TreeNode:
     def __init__(self,data,children=[]):
          self.data=data
          self.children=children
     def __str__(self,level=0):
          ret= "___"*level +str(self.data )+"\n"
          for child in self.children:
               ret += child.__str__(level+1)
          return ret
     def addChild(self,TreeNode):
          self.children.append(TreeNode)

tree=TreeNode("Drinks",[])
cold=TreeNode("Cold",[])
hot=TreeNode("Hot",[])
tea=TreeNode("tea",[])
coffee=TreeNode("coffee",[])
pepsi=TreeNode("pepsi",[])
cocacola=TreeNode("cocacola",[])
cold.addChild(pepsi)
cold.addChild(cocacola)
hot.addChild(tea)
hot.addChild(coffee)
tree.addChild(cold)
tree.addChild(hot)
print(tree)



