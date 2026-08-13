# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque

# -----------------------------------------------------------------
# First Approach: Store TreeNode in adjacency list
# -----------------------------------------------------------------

# This is totally valid approach
# But as Constraints as - All the values Node.val are unique
# so, storing a TreeNode in the adj is overspacing
# def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
#         adj = defaultdict(list)
 
#         def dfs(root):
#             if not root: return

#             if root.left:
#                 adj[root.left].append(root)
#                 adj[root].append(root.left)
#                 dfs(root.left)

#             if root.right:
#                 adj[root.right].append(root)
#                 adj[root].append(root.right)
#                 dfs(root.right)
#         dfs(root)
        
#         q = deque([target])
#         vis = {target.val}
#         d = 0

#         ans = []
#         while q:
#             if d == k:
#                 for node in q:
#                     ans.append(node.val)
#                 return ans
#             for _ in range(len(q)):
#                 node = q.popleft()
#                 for it in adj[node]:
#                     if it.val not in vis:
#                         vis.add(it.val)
#                         q.append(it)

#             d += 1

#         return []

# -----------------------------------------------------------------
# Second Approach: Only store values in adjacency list
# -----------------------------------------------------------------

# It only works because Constraints says "All the values Node.val are unique"
# if it wasn't there and there can be same value then this will fail and first approach will be the solution.


# The Intuition for both approaches is same:
# 1. create an adjacency list but store it like an unordered graph, means parent will store child as well as child will store parent
# 2. try to create a graph from adjacency list
# 3. as we only care about kth nodes so build only upto kth phase and return the last queue values
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)
 
        def dfs(root):
            if not root: return

            if root.left:
                adj[root.left.val].append(root.val)
                adj[root.val].append(root.left.val)
                dfs(root.left)

            if root.right:
                adj[root.right.val].append(root.val)
                adj[root.val].append(root.right.val)
                dfs(root.right)
        dfs(root)
        
        q = deque([target.val])
        vis = {target.val}
        d = 0
        while q and d < k:
            for _ in range(len(q)):
                node = q.popleft()
                for it in adj[node]:
                    if it not in vis:
                        vis.add(it)
                        q.append(it)

            d += 1

        return list(q)