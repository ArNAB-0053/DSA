'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def insert(self, root: 'Node', key: int) -> 'Node':
        if not root: return Node(key)
        
        curr = root
        while curr:
            if curr.data > key:
                if curr.left is None:
                    curr.left = Node(key)
                    break
                else:
                    curr = curr.left
            elif curr.data < key:
                if curr.right is None:
                    curr.right = Node(key)
                    break
                else:
                    curr = curr.right
            else:
                return root
                    
        return root
            
        