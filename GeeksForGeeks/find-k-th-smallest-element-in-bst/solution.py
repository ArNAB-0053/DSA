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
        ans, itr = -1, 0
        def inorder(root):
            nonlocal ans, itr
            if not root or ans != -1: return
            
            inorder(root.left)
            itr += 1
            if itr == k:
                ans = root.data
                return
            inorder(root.right)
            
        inorder(root)
        return ans