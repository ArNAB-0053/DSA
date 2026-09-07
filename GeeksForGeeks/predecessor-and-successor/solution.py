'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def findPreSuc(self, root, key):
        if not root: return None
        
        pred, succ = None, None
        curr = root
        
        while curr:
            if curr.data > key:
                succ = curr
                curr = curr.left
            elif curr.data < key:
                pred = curr
                curr = curr.right
            else:
                left = curr.left
                right = curr.right
                
                while left is not None:
                    pred = left
                    left = left.right
                while right is not None:
                    succ = right
                    right = right.left
                
                break
                
        return [pred, succ]
                
        