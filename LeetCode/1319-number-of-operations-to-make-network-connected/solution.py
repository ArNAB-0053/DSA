class DSU:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.size = [1]*n
        # self.extra = 0
        self.components = n

    def find(self, x: int):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a: int, b: int):
        pa, pb = self.find(a), self.find(b)

        if pa == pb:
            # self.extra += 1
            return
        
        self.components -= 1
        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa

        self.parents[pb] = pa
        self.size[pa] += self.size[pb]

    # O(1) getter.
    # Returning the component count maintained during union operations.
    # Could directly access dsu.components in Python, but keeping a method provides a cleaner DSU interface.
    def noOfComponents(self):
        return self.components

    # O(1) getter.
    # Not needed for LeetCode 1319 after the len(connections) < n - 1 check, 
    # but useful in other DSU problems involving redundant edges/cycle detection.
    # def getExtraNodes(self):
    #     return self.extra

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1

        dsu = DSU(n)

        for u, v in connections:
            dsu.union(u, v)

        cntComp = dsu.noOfComponents()

        # here don't need this cause
        # we are already checking len(connections) < n-1
        # cntExtra = dsu.getExtraNodes()

        # so also don't need this check
        # if cntExtra >= cntComp - 1:
        #     return cntComp - 1
        # return -1
        
        return cntComp - 1