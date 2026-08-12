'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        if not root: return True
        
        if not root.left and not root.right: return True
        
        left = root.left.data if root.left else 0
        right = root.right.data if root.right else 0
        
        if root.data != left + right:
            return False
        
        return (
                self.isSumProperty(root.left) and
                self.isSumProperty(root.right)
            )