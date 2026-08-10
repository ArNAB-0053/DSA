'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

from collections import deque

class Solution:
    def bottomView(self, root):
        if not root: return []
        
        q  = deque([(root, 0)]) # node, column
        mapp = {}
        
        while q:
            node, col = q.popleft()
            mapp[col] = node.data
            
            if node.left: q.append((node.left, col-1))
            if node.right: q.append((node.right, col+1))
        
        bottom_view = []
        for key in sorted(mapp):
            bottom_view.append(mapp[key])
            
        return bottom_view