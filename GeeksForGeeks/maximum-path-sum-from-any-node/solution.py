''' Structure of binary tree node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def maxSum(self, root):
        if not root: return 0
        le = max(0, self.maxSum(root.left))
        ri = max(0, self.maxSum(root.right))
        
        self.summ = max(le+ri+root.data, self.summ)
        
        return root.data + max(le, ri)
        
    def findMaxSum(self, root): 
        self.summ = root.data
        self.maxSum(root)
        return self.summ
        