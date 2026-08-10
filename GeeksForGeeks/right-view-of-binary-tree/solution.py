'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def rightView(self, root):
        if not root: return []
        q = deque([(root, 0)]) # node, row
        
        right_view = []

        while q:
            size = len(q)
            for i in range(size):
                node, row = q.popleft()
            
                if i == size - 1:
                    right_view.append(node.data)
                    
                if node.left: q.append((node.left, row+1))
                if node.right: q.append((node.right, row+1))
            
        return right_view