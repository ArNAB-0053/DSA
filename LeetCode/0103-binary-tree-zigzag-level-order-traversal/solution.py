# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q = deque([root])
        res = []
        ltr = True # ltr -> left to right

        while q:
            size = len(q)
            level = [0] * size

            for i in range(size):
                node = q.popleft()
                
                # if this pass is ltr -> start adding from left
                # else -> start adding from right
                # it helps avoiding reversing the whole level array
                if ltr:
                    level[i] = node.val
                else:
                    level[size-i-1] = node.val

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            res.append(level)
            ltr = not ltr

        return res