''' Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def minTime(self, root, target):
        parent = {}
        
        target_node = None
        
        def dfs(node, par=None):
            nonlocal target_node
            if not node: return 
        
            if node.data == target:
                target_node = node
        
            parent[node] = par
            
            if node.left: dfs(node.left, node)
            if node.right: dfs(node.right, node)
            
        dfs(root)
        
        q = deque([target_node])
        visited = {target_node}
        
        height = -1
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                    
                neighbors = [
                    node.left,
                    node.right,
                    parent[node]
                ]
                
                for neighbor in neighbors:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
                
            
            height += 1
            
        return height