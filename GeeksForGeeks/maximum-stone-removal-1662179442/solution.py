class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)

        if pa == pb:
            return

        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa

        self.parents[pb] = pa
        self.size[pa] += self.size[pb]

class Solution:
    def maxRemove(self, stones):
        n = len(stones)
        # stores the max row and col index
        maxRow, maxCol = 0, 0
        for row, col in stones:
            maxRow = max(maxRow, row)
            maxCol = max(maxCol, col)
        
        # DSU nodes represent rows and columns
        # Row nodes: [0 ... maxRow]
        # Col nodes: [maxRow + 1 ... maxRow + maxCol + 1]
        # This guarantees row and column indices never collide
        dsu = DSU(maxRow + maxCol + 2)

        # Track nodes that actually appear in the input
        # Unused DSU nodes must not be counted as components
        used = set()
        for row, col in stones:
            # the current col node is current col + maxRow + 1
            col += maxRow + 1
            dsu.union(row, col)
            # row and col that have been used for union
            used.add(row)
            used.add(col)
        # Each connected component contributes exactly one root
        # Count roots only among nodes that appear in stones
        cntRoots = 0
        for root in used:
            if dsu.find(root) == root:
                cntRoots += 1
        # In a component with k stones, we can remove k - 1 stones.
        # Therefore, the maximum removable stones equal:
        # total_stones - number_of_connected_components
        return n - cntRoots
        