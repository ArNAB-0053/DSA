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
        if not root: return []
        q = deque([root])
        res = []
        ltr = True # ltr -> eft to right
        while q:
            size = len(q)
            level = [0] * size
            
            for i in range(size):
                node = q.popleft()
                
                # avoiding traversing later on with this optimization
                # for ltr it will append from the left side
                # whereas if not ltr then from right side
                # it helps avoiding reversing the whole level array
                if ltr:
                    level[i] = node.data
                else:
                    level[size-i-1] = node.data
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
        
            ltr = not ltr
            # as it doesn't want a array of array output but a single output
            # we are only adding the values to res
            res += level
        
        return res