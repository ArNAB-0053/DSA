''' Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def verticalOrder(self, root): 
        if not root: return []
        q = deque([(root, 0)])
        columns = {}
        
        while q:
            node, col = q.popleft()
            
            if col not in columns:
                columns[col] = []
                
            columns[col].append(node.data)
            
            if node.left: q.append((node.left, col - 1))
            if node.right: q.append((node.right, col + 1))
            
        res = []
        for col in sorted(columns):
            res.append(columns[col])
        
        return res