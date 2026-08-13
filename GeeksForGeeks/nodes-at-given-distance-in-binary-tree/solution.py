'''
Structure of Binary Tree Node
 class Node:
     def __init__(self, val):
         self.data = val
        self.left = None
        self.right = None
'''

# go to -> https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# for detailed breakdown

from collections import defaultdict, deque

class Solution:
    def kDistanceNodes(self, root, targetVal, k):
        parents = {}
        
        target = None

        # parent dict creating funtion   
        def dfs(node, parent = None):
            nonlocal target
            if not node: return
            if node.data == targetVal:
                target = node
            parents[node] = parent
            if node.left: dfs(node.left, node)
            if node.right: dfs(node.right, node)
        
        # fn call
        dfs(root)
        
        # actual BFS (same as BFS on graph)
        q = deque([target])
        vis = {target}
        d = 0 # distance
        while q:
            if d == k:
                return sorted([node.data for node in q])

            for _ in range(len(q)):
                node = q.popleft()

                neighbors = [
                    node.left,
                    node.right,
                    parents[node]
                ]

                for neighbor in neighbors:
                    if neighbor and neighbor not in vis:
                        vis.add(neighbor)
                        q.append(neighbor)

            d += 1

        return []
        