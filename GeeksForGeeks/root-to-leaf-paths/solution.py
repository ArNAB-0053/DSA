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
        def dfs(node):
            temp.append(node.data)
            
            if self.isLeaf(node):
                res.append(temp.copy())
            else:
                if node.left: dfs(node.left)
                if node.right: dfs(node.right)
            temp.pop()
            
            
        dfs(root)
        return res