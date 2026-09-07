'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def preToBST(self, preorder):
        i = 0
        def buildBST(maxx):
            nonlocal i

            # Base Cases
            if i == len(preorder) or preorder[i] > maxx:
                return None

            node = Node(preorder[i])

            # iterator - determines the item
            i = i+1

            # for left, parent becomes the maxx
            node.left = buildBST(node.data)
            # for right, maxx stays as maxx
            node.right = buildBST(maxx)

            return node

        return buildBST(float('inf'))