'''
# Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def maxWidth(self, root):
        if not root: return 0
        
        q = deque([root]) # node, index
        max_width = len(q)
        
        while q:
            size = len(q)
            max_width = max(max_width, size)
            
            for _ in range(size):
                node = q.popleft()
                    
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
            
        return max_width