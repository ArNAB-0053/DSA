# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self, root):
        return not root.left and not root.right
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return []

        ## Using list
        # res, temp = [], []
        
        # def dfs(node):
        #     temp.append(node.val)

        #     if self.isLeaf(node):
        #         # s = ""
        #         # for ch in temp:
        #         #     arw = "->" if s else ""
        #         #     s = s + arw + str(ch)
        #         # res.append(s)

        #         # in simple one line
        #         res.append("->".join(map(str, temp)))
        #     else:
        #         if node.left: dfs(node.left)
        #         if node.right: dfs(node.right)
            
        #     temp.pop()

        # dfs(root)
        # return res

        ## Using string intead
        res = []

        def dfs(node, path):
            path += str(node.val)

            if self.isLeaf(node):
                res.append(path)
                return 

            path += '->'

            if node.left: dfs(node.left, path)
            if node.right: dfs(node.right, path)

        dfs(root, "")
        return res
