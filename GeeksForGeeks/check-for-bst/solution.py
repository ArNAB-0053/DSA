'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isBST(self, root: 'Node') -> bool:
        prev = -1
        
        def inorder(root):
            nonlocal prev
            
            if not root: return True
            
            left = inorder(root.left)
            if not left:
                return False
            
            if prev >= root.data:
                return False
                
            prev = root.data
            
            right = inorder(root.right)
            if not right:
                return False
                
            return True
            
        return inorder(root)
        