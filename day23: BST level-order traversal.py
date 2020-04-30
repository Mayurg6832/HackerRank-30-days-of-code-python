import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        if type(root) is list:
            roots=root
        else:
            roots=[root]
        new_lst=[]
        nodes=[]
        if not roots:
            return
        else:
            for node in roots:
                nodes.append(node.data)
                if node.left is not None:
                    new_lst.append(node.left)
                if node.right is not None:
                    new_lst.append(node.right)
            for j in nodes:
                print(j,end=" ")
        self.levelOrder(new_lst)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
