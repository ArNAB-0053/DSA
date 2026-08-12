# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        q = deque([(root, 0)])
        max_width = 0

        while q:     
            size = len(q)
            minn = q[0][1]
            first = last = 0
            for i in range(size):
                node, idx = q.popleft()
                curr_id = idx - minn          

                if i == 0: first = curr_id
                if i == size - 1: last = curr_id

                if node.left: q.append((node.left, curr_id*2 + 1))
                if node.right: q.append((node.right, curr_id*2 + 2))
            max_width = max(max_width, last - first + 1)
        return max_width