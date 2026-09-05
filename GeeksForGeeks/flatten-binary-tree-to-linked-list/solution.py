""" Binary Tree Node Structure
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""
class Solution:
    def flatten(self, root):
        # ==============================================
        # Recursion Approach - O(n) Time | O(n) Space
        # ==============================================
        # prev = None

        # def do_flatten(node):
        #     nonlocal prev

        #     if node is None: return 

        #     # go right
        #     do_flatten(node.right)
        #     # go left
        #     do_flatten(node.left)

        #     # connect node right to prev
        #     node.right = prev
        #     # disconnect left
        #     node.left = None

        #     # make prev as current node
        #     prev = node

        # do_flatten(root)

        # ========================================
        # Using Stack - O(n) Time | O(n) Space
        # ========================================
        # if not root: return

        # stack = [root]

        # while stack:
        #     # get top-most element and pop it out
        #     curr = stack.pop()
        #     # append right
        #     if curr.right: stack.append(curr.right)
        #     # append left
        #     if curr.left: stack.append(curr.left)

        #     # the order of first right then left ensures left will be on top first when popping

        #     # if stack not null
        #     # connect curr right to top of stack
        #     if stack: curr.right = stack[-1]
        #     # and disconnect curr left
        #     curr.left = None


        # ========================================
        # Morris Traversal - O(n) Time | O(1) Space
        # ========================================
        if not root: return

        curr = root

        while curr:
            # when curr has left
            if curr.left:
                # prev is curr left
                prev = curr.left

                # move to the right most
                while prev.right:
                    prev = prev.right

                # connect prev right with curr right
                prev.right = curr.right
                # curr right now will be curr left
                curr.right = curr.left
                # disconnect curr left
                curr.left = None

            # move curr
            curr = curr.right
        