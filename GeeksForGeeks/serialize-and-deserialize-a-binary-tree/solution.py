''' Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque

# Using BFS

class Solution:
    def serialize(self, root):
        if not root: return []

        q = deque([root])
        ans = []

        while q:
            node = q.popleft()
            
            if node:
                ans.append(node.data)
                q.append(node.left)
                q.append(node.right)
                
            else: 
                ans.append("N")
            
        while ans and ans[-1] == "N":
            ans.pop()

        return ans

    def deSerialize(self, arr):
        if not arr: return None
        
        root = Node(arr[0])
        q = deque([root])

        i = 1
        while q and i < len(arr):
            node = q.popleft()
            
            if arr[i] != "N":
                left = Node(arr[i])
                node.left = left
                q.append(left)
                
            i += 1
            
            if i < len(arr) and arr[i] != "N":
                right = Node(arr[i])
                node.right = right
                q.append(right)
                
            i += 1
                
        return root
            