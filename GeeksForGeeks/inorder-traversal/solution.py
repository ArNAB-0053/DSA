''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

# It can be done using several approach RECURSION or Using STACK

# BUT

# I am doing it here,
# Using MORRIS TRAVERSAL TECHNIQUE

# MORRIS TRAVERSAL TECHNIQUE uses O(n) time and O(1) space
# where both recursion and stack takes O(n) time ans space
# so it a space optimisation technique

# Mainly here we create a temporary thread between nodes.
class Solution:
    def inOrder(self, root):
        curr = root # intial
        ans = []
        
        while curr:
            # CASE - 1 : when left doesn't exist
            if curr.left is None:
                # add value to ans
                ans.append(curr.data)
                # move curr to right
                curr = curr.right
                
            # CASE - 2 : left exists
            else:
                prev = curr.left # previous / predecessor
                
                # get the rightmost node
                # when prev.right exists and is not equals to curr
                while prev.right and prev.right != curr:
                    prev = prev.right
                    
                if prev.right is None:
                    # create a temporary thread
                    prev.right = curr
                    # move curr to left
                    curr = curr.left 
                else:
                    # remove the thread
                    prev.right = None
                    # add value to ans
                    ans.append(curr.data)
                    # move curr to right
                    curr = curr.right
                    
        return ans
        