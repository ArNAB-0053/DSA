# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://www.youtube.com/watch?v=UmJT3j26t1I&list=PLkjdNRgDmcc0Pom5erUBU4ZayeU9AyRRu&index=48
# for revision


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = 0
        def buildBST(maxx):
            nonlocal i

            # Base Cases
            if i == len(preorder) or preorder[i] > maxx:
                return None

            node = TreeNode(preorder[i])

            # iterator - determines the item
            i = i+1

            # for left, parent becomes the maxx
            node.left = buildBST(node.val)
            # for right, maxx stays as maxx
            node.right = buildBST(maxx)

            return node

        return buildBST(float('inf'))