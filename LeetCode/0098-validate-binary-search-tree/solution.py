# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        # min-max approach   
        # def isValid(node, minn, maxx):
        #     if not node:
        #         return True
            
        #     if not (minn < node.val < maxx):
        #         return False
            
        #     left = isValid(node.left, minn, node.val)
        #     right = isValid(node.right, node.val, maxx)

        #     return left and right
        
        # return isValid(root, float('-inf'), float('inf'))

        # Optimised Inorder traversal - store only previous element
        # we know for BST Inorder traversal gives sorted array - so can do just get the Inorder traversal and check sorted or not, but Optimised is only check previous element is smaller than the current or not.
        prev = float('-inf')

        def inorder(node):
            nonlocal prev

            if not node:
                return True
            
            left = inorder(node.left)
            if not left:
                return False
            
            if node.val <= prev:
                return False
            
            prev = node.val

            right = inorder(node.right)
            if not right:
                return False
            
            return True
        return inorder(root)