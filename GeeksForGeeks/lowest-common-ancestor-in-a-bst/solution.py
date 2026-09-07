'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def findLCA(self, root: 'Node', n1: 'Node', n2: 'Node') -> 'Node':
        if n1.data > root.data and n2.data > root.data:
            return self.findLCA(root.right, n1, n2)
            
        elif n1.data < root.data and n2.data < root.data:
            return self.findLCA(root.left, n1, n2)
            
        return root
        