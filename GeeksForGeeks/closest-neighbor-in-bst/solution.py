'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        floor = -1
        
        while root:
            if root.data == k:
                return k
            
            if root.data < k:
                floor = root.data
                root = root.right
                
            else:
                root = root.left
                
        return floor
        