class Solution:
    # dfs on adjacency matrix
    # def dfs(self, vis, adjMat, node):
    #     """

    #     Args:
    #         vis: Visited Array
    #         adjMat: Adjacency Matrix
    #         node: Node that need visiting

    #     """
    #     vis[node] = True

    #     for nei in range(len(adjMat)):
    #         if adjMat[node][nei] == 1 and not vis[nei]:
    #             self.dfs(vis, adjMat, nei)

    # def findCircleNum(self, isConnected: List[List[int]]) -> int:
    #     """

    #     Args:
    #         isConnected: Adjacency Matrix

    #     """
    #     vis = [False] * len(isConnected)
    #     c = 0

    #     for i in range(len(vis)):
    #         if not vis[i]:
    #             self.dfs(vis, isConnected, i)
    #             c += 1
        
    #     return c


    # -----------------------------------------------
    #                     Using DSU
    # -----------------------------------------------
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        dsu = DSU(n)

        for row in range(n):
            for col in range(n):
                if isConnected[row][col] == 1:
                    dsu.union(row, col)

        return dsu.getTotalUniqueParents()

# The main 
class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x]) # path compression

        return self.parents[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)

        if pa == pb:
            return
        
        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa

        self.parents[pb] = pa
        self.size[pa] += self.size[pb]

    def getTotalUniqueParents(self):
        cnt = 0
        for i in range(len(self.parents)):
            if self.parents[i] == i:
                cnt += 1

        return cnt