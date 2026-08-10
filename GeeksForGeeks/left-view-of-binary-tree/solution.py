''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''
from collections import deque
class Solution:
    def leftView(self, root):
        if not root: return []
        q = deque([(root, 0)]) # node, row
        
        left_view = []

        while q:
            for i in range(len(q)):
                node, row = q.popleft()
            
                if i == 0:
                    left_view.append(node.data)
                    
                if node.left: q.append((node.left, row+1))
                if node.right: q.append((node.right, row+1))
            
        return left_view