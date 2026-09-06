'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,root, x):
        if not root: return
        ceil = 9999
        
        def func(root):
            nonlocal ceil
            if not root: return
        
            if x == root.data:
                ceil = root.data
                return
            
            if ceil > root.data and root.data > x:
                ceil = root.data
            
            if x < root.data and root.left:
                func(root.left)
            elif x > root.data and root.right: 
                func(root.right)
        
        func(root)
        
        if ceil == 9999: return -1
        return ceil
            
        