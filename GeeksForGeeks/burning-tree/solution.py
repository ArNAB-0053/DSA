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
        # Intuition
        
        # - store parent -> child in a map
        # - try to create a proper undirected graph from it
        # - find out the height based on depth
        
        parent = {} # stores parent -> child
        
        target_node = None # given target is value, but I need node
        
        # TREE DFS
        def dfs(node, par=None):
            nonlocal target_node
            if not node: return 
        
            # gives the targeted node
            if node.data == target:
                target_node = node
            
            # stores parent -> child
            parent[node] = par
            
            if node.left: dfs(node.left, node)
            if node.right: dfs(node.right, node)
        
        # fn call
        dfs(root)
        
        # from starts GRAPH BFS traversal
        q = deque([target_node])
        visited = {target_node}
        
        height = -1 # as it counts the edge
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                    
                # those are all the neighbors
                # or rather the traversal possible only to these
                neighbors = [
                    node.left,
                    node.right,
                    parent[node]
                ]
                
                for neighbor in neighbors:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
                
            # height updation
            height += 1
            
        return height