'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def kthSmallest(self, root, k): 
        itr = 0
        def inorder(root):
            nonlocal itr
            if not root: return None
            
            left = inorder(root.left)
            
            if left is not None: return left
            
            itr += 1
            if itr == k:
                return root.data
                
            return inorder(root.right)
            
        ans = inorder(root)
        
        if ans is not None: return ans
        return -1