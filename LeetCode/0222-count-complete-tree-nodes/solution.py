# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countLeftHeight(self, root):
        count = 0
        while root:
            count += 1
            root = root.left
        return count

    def countRightHeight(self, root):
        count = 0
        while root:
            count += 1
            root = root.right
        return count

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        left_height = self.countLeftHeight(root)
        right_height = self.countRightHeight(root)

        if left_height == right_height:
            return (2 ** left_height) - 1

        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1