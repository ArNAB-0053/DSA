'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
class Solution:
    # check is it a leaf node or not
    def isLeaf(self, node):
        if node.left or node.right:
            return False
        return True
        
    # added left sided nodes of root to res except leaf nodes
    def addLeftNodes(self, root):
        curr = root.left
        
        while curr:
            if not self.isLeaf(curr):
                self.res.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
    
    # adds only leaf nodes to res
    def addLeafNode(self, root):
        if self.isLeaf(root):
            self.res.append(root.data)
            return
        if root.left: self.addLeafNode(root.left)
        if root.right: self.addLeafNode(root.right)
    
    # add right sided node of root to res except leaf nodes
    def addRightNodes(self, root):
        # as it is acyclic boundary
        # we have to reverse the right nodes
        # so we are using temp and later add it's reversed value to res
        temp = []
        curr = root.right
        
        while curr:
            if not self.isLeaf(curr):
                temp.append(curr.data)
                
            if curr.right: curr = curr.right
            else: curr = curr.left
        
        # adding temp's reverse value to res
        self.res += temp[::-1]
        
    def boundaryTraversal(self, root):
        # if no root node
        if not root: return []
        
        # if root node itself a leaf node
        if self.isLeaf(root): return [root.data]
        
        # initializeing res with root.data
        self.res = [root.data]
        
        # calling all the helper fns
        
        # as it want acyclic boundary traversal
        # we do - 
        # 1. all left nodes
        # 2. all leaf nodes
        # 3. all right nodes(reverse order)
        self.addLeftNodes(root)     #1
        self.addLeafNode(root)      #2
        self.addRightNodes(root)    #3
        
        return self.res
        