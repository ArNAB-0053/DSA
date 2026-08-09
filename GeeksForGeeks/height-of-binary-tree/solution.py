''' Structure of Binary Tree Node
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def height(self, root):
        if not root: return -1
        left = self.height(root.left)
        right = self.height(root.right)
        return 1 + max(left, right)