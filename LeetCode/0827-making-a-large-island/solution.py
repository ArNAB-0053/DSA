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

    def getSize(self, x):
        return self.size[x]

class Solution:
    def isValid(self, nrow, ncol, n):
        return nrow >= 0 and nrow < n and ncol >= 0 and ncol < n

    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dsu = DSU(n*n)

        dirs = ((-1, 0), (0,-1), (1,0), (0,1))
        mx = 0

        # Step - 1
        # Build connected components of all existing land cells (1s)
        # using DSU. Each component represents an island and
        # DSU.size[root] stores the island size.
        for row in range(n):
            for col in range(n):
                # if grid[row][col] == 0 -> skip
                if not grid[row][col]:
                    continue
                for dr, dc in dirs:
                    nrow, ncol = dr + row, dc + col
                    if self.isValid(nrow, ncol, n) and grid[nrow][ncol]:
                        node = row * n + col
                        adjNode = nrow * n + ncol
                        dsu.union(node, adjNode)
        # Step - 2
        # Try converting every 0 into a 1.
        # Collect all unique neighboring island components,
        # sum their sizes and add 1 for the flipped cell.
        for row in range(n):
            for col in range(n):
                if grid[row][col]:
                    continue
                components = set()
                for dr, dc in dirs:
                    nrow, ncol = dr + row, dc + col
                    if self.isValid(nrow, ncol, n) and grid[nrow][ncol]:
                        # Store unique neighboring island roots to avoid counting the same island twice
                        components.add(dsu.find(nrow * n + ncol))

                total = 1
                for parent in components:
                    total += dsu.getSize(parent)

                mx = max(total, mx)

        # Step - 3
        # Edge case: grid contains only 1s.
        # In that case Step 2 never runs, so the answer is
        # simply the size of the largest existing island.
        for i in range(n*n):
            mx = max(mx, dsu.getSize(dsu.find(i)))

        return mx
