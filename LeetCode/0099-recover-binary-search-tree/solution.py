# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev, first, second = None, None, None
        
        # Using Recursive Inorder
        # can be solve using "Morris Traversal" if we wanna exclude the O(h) recursion extra space, but for simplicity I didn't. 
        def inorder(root):
            nonlocal prev, first, second
            if not root:
                return
            # 1. go left
            inorder(root.left)
            # 2. work with val
            # if prev is not None and prev val > curr val
            # then we can say there is a problem
            if prev and prev.val > root.val:
                # first problem
                if first is None:
                    first = prev
                # there are two cases
                # 1. immediate neighbor is the second problem
                # 2. second problem happens later on
                second = root
            prev = root
            # 3. go right
            inorder(root.right)
        inorder(root)

        if first and second:
            first.val, second.val = second.val, first.val