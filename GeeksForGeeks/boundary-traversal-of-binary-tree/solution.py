'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
class Solution:
    def isLeaf(self, node):
        if node.left or node.right:
            return False
        return True
        
    def addLeftNodes(self, root):
        curr = root.left
        
        while curr:
            if not self.isLeaf(curr):
                self.res.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
        
    def addLeafNode(self, root):
        if self.isLeaf(root):
            self.res.append(root.data)
            return
        if root.left: self.addLeafNode(root.left)
        if root.right: self.addLeafNode(root.right)
        
    def addRightNodes(self, root):
        temp = []
        curr = root.right
        
        while curr:
            if not self.isLeaf(curr):
                temp.append(curr.data)
                
            if curr.right: curr = curr.right
            else: curr = curr.left
            
        self.res += temp[::-1]
        
    def boundaryTraversal(self, root):
        if not root: return []
        
        if self.isLeaf(root): return [root.data]
        
        self.res = [root.data]
        self.addLeftNodes(root)
        self.addLeafNode(root)
        self.addRightNodes(root)
        
        return self.res
        