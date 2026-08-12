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
        
        q = deque([(root, 0)]) # node, index
        max_width = 0

        while q:     
            size = len(q)
            minn = q[0][1]
            first = last = 0 # first and last index
            for i in range(size):
                node, curr_idx = q.popleft()

                # normalization: (-minn) will start indexing for the current label from 0

                # without normalization, indices can grow exponentially with depth (e.g. 2*i+1 / 2*i+2), especially in a deep/skewed tree. Very large integer operations can become expensive.
                
                # by shifting the current level to start from 0, we keep the indices small while preserving the relative positions needed to calculate the width.
                curr_idx -= minn          

                if i == 0: first = curr_idx
                if i == size - 1: last = curr_idx

                # for a binary tree
                # if root having index 0 suppose that is curr_id (curr_idx = 0)
                # then the left child will have 2 * curr_idx + 1 => 1
                # and the right child will have 2 * curr_idx + 2 => 2
                if node.left: q.append((node.left, curr_idx*2 + 1))
                if node.right: q.append((node.right, curr_idx*2 + 2))

            max_width = max(max_width, last - first + 1)
            
        return max_width