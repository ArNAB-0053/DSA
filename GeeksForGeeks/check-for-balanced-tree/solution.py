''' Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def maxDepth(self, root):
        if not root: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        if abs(left - right) > 1: return -1
        
        if left == -1 or right == -1: return -1
        
        return 1 + max(left, right)
        
    def isBalanced(self, root):
        return self.maxDepth(root) != -1