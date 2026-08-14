# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Intuition
        
    # - store parent -> child in a map
    # - try to create a proper undirected graph from it
    # - find out the height based on depth

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = {} # stores parent -> child
        start_node = None # as start is a value, but I need it as node

        # TREE DFS
        def dfs(root, par=None):
            nonlocal start_node
            if not root: return

            if root.val == start: 
                start_node = root

            # storing to parent map
            parent[root] = par

            if root.left: dfs(root.left, root)
            if root.right: dfs(root.right, root)

        # fn call
        dfs(root)

        # GRAPH BFS
        q = deque([start_node])
        visited = {start_node}

        height = -1 # as it counts no. of edges

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                # can traverse only these nodes
                neighbors = [
                    node.left,
                    node.right,
                    parent[node]
                ]

                for nei in neighbors:
                    if nei and nei not in visited:
                        visited.add(nei)
                        q.append(nei)

            height += 1

        return height

