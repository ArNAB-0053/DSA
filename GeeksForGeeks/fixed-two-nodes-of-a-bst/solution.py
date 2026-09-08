''' 
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''        
class Solution:
    def correctBST(self, root: 'Node') -> 'Node':
        prev, first, second = None, None, None

        # Using Recursive Inorder
        # can be solve using "Morris Traversal",
        # if we wanna exclude the O(h) recursion extra space, but for simplicity I didn't. 
        def inorder(root):
            nonlocal prev, first, second
            if not root:
                return
            # 1. go left
            inorder(root.left)
            # 2. work with val
            # if prev is not None and prev val > curr val
            # then we can say there is a problem
            if prev and prev.data > root.data:
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
            first.data, second.data = second.data, first.data
            
        return root
        