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
        # -----------------------------------
        # USING RECURSIVE APPROACH
        # -----------------------------------
        # TC: O(h) - best/average case
        #     O(n) - worst case
        # SC: O(h) - if considering recursion stack space
        #     O(1) - if not considering that
        
        # if n1.data > root.data and n2.data > root.data:
        #     return self.findLCA(root.right, n1, n2)
            
        # elif n1.data < root.data and n2.data < root.data:
        #     return self.findLCA(root.left, n1, n2)
            
        # return root
        
        # -----------------------------------
        # USING WHILE LOOP
        # -----------------------------------
        # TC: O(h) - best/average case
        #     O(n) - worst case
        # SC: O(1)
        
        curr = root
        
        while curr:
            if n1.data < curr.data and n2.data < curr.data:
                curr = curr.left
                
            elif n1.data > curr.data and n2.data > curr.data:
                curr = curr.right
                
            else:
                return curr
                
        return None
        