"""
Definition of Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
from collections import deque
class Solution:
    def isLeaf(self, node):
        if node.left or node.right:
            return False
        return True
        
    def paths(self, root):
        if not root: return []
        
        res, temp = [], []
        def inorder(node):
            temp.append(node.data)
            
            if self.isLeaf(node):
                res.append(temp.copy())
            else:
                if node.left: inorder(node.left)
                if node.right: inorder(node.right)
            temp.pop()
            
            
        inorder(root)
        return res