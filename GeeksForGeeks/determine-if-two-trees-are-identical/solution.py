'''
class Node:
    def _init_(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isIdentical(self, r1, r2):
        if not r1 or not r2:
            return r1 == r2
        return (
                r1.data == r2.data and
                self.isIdentical(r1.left, r2.left) and
                self.isIdentical(r1.right, r2.right)
            )