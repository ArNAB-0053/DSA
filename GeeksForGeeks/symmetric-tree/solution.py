'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isSymmetric(self, root):
        if not root: return True
        if not root.left and not root.right: return True
        if not root.left or not root.right: return False
        
        left = root.left
        right = root.right
        
        def solve(left, right):
            if not left or not right:
                return left == right
                
            if left.data != right.data: return False
            
            return (
                    solve(left.left, right.right) 
                    and
                    solve(left.right, right.left)
                )
            
        
        return solve(left, right)