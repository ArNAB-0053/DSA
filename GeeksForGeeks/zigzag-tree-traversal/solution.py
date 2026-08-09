''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def zigZagTraversal(self, root):
        q = deque([root])
        res = []
        ltr = True
        while q:
            size = len(q)
            level = [0] * size
            
            for i in range(size):
                node = q.popleft()
                
                if ltr:
                    level[i] = node.data
                else:
                    level[size-i-1] = node.data
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
        
            ltr = not ltr
            res += level
        
        return res