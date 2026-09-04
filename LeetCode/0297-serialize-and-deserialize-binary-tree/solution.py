# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

# Using BFS
class Codec:

    def serialize(self, root):
        res = []
        def solve(root):
            nonlocal res
            if not root:
                res.append('null')
                return
            
            res.append(str(root.val))
            solve(root.left)
            solve(root.right)
        solve(root)
        return ",".join(res)
        

    def deserialize(self, data):
        if not data:
            return None

        vals = data.split(',')
        que = deque(vals)

        def dfs():
            val = que.popleft()

            if val == 'null':
                return None
            
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))