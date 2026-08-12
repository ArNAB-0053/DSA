''' Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def lca(self, root, n1, n2):
        if not root or root.data == n1 or root.data == n2:
            return root
        
        left = self.lca(root.left, n1, n2)
        right = self.lca(root.right, n1, n2)
        
        if not left: return right
        elif not right: return left
        else: return root

