'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def topView(self, root):
        if not root: return []
        q = deque([(root, 0)]) # node, column
        
        mapp = {}
        while q:
            node, col = q.popleft()
            
            if col not in mapp:
                mapp[col] = node.data
                
            if node.left: q.append((node.left, col-1))
            if node.right: q.append((node.right, col+1))
            
        
        top_view = []
        for key in sorted(mapp):
            top_view.append(mapp[key])
            
        return top_view