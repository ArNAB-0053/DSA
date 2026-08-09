''' Structure of binary tree Node 
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def maxDepth(self, root):
        if not root: return 0
        le = self.maxDepth(root.left)
        ri = self.maxDepth(root.right)
        self.diameter = max(le+ri, self.diameter)
        return 1 + max(le, ri)
        
    def diameter(self, root):
        self.diameter = 0
        self.maxDepth(root)
        return self.diameter
        
        