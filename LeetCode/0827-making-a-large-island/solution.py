# --------------------------------------------
#                 DSU APPROACH
# --------------------------------------------
# TC: O(N² · α(N²)) -> O(N²)
# SC: O(N²)
# --------------------------------------------
# class DSU:
#     def __init__(self, n):
#         self.parents = list(range(n))
#         self.size = [1] * n

#     def find(self, x):
#         if self.parents[x] != x:
#             self.parents[x] = self.find(self.parents[x])
#         return self.parents[x]

#     def union(self, a, b):
#         pa, pb = self.find(a), self.find(b)

#         if pa == pb:
#             return

#         if self.size[pa] < self.size[pb]:
#             pa, pb = pb, pa

#         self.parents[pb] = pa
#         self.size[pa] += self.size[pb]

#     def getSize(self, x):
#         return self.size[x]

# class Solution:
#     def isValid(self, nrow, ncol, n):
#         return nrow >= 0 and nrow < n and ncol >= 0 and ncol < n

#     def largestIsland(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         dsu = DSU(n*n)

#         dirs = ((-1, 0), (0,-1), (1,0), (0,1))
#         mx = 0

#         # Step - 1
#         # Build connected components of all existing land cells (1s)
#         # using DSU. Each component represents an island and
#         # DSU.size[root] stores the island size.
#         for row in range(n):
#             for col in range(n):
#                 # if grid[row][col] == 0 -> skip
#                 if not grid[row][col]:
#                     continue
#                 for dr, dc in dirs:
#                     nrow, ncol = dr + row, dc + col
#                     if self.isValid(nrow, ncol, n) and grid[nrow][ncol]:
#                         node = row * n + col
#                         adjNode = nrow * n + ncol
#                         dsu.union(node, adjNode)
#         # Step - 2
#         # Try converting every 0 into a 1.
#         # Collect all unique neighboring island components,
#         # sum their sizes and add 1 for the flipped cell.
#         for row in range(n):
#             for col in range(n):
#                 if grid[row][col]:
#                     continue
#                 components = set()
#                 for dr, dc in dirs:
#                     nrow, ncol = dr + row, dc + col
#                     if self.isValid(nrow, ncol, n) and grid[nrow][ncol]:
#                         # Store unique neighboring island roots to avoid counting the same island twice
#                         components.add(dsu.find(nrow * n + ncol))

#                 total = 1
#                 for parent in components:
#                     total += dsu.getSize(parent)

#                 mx = max(total, mx)

#         # Step - 3
#         # Edge case: grid contains only 1s.
#         # In that case Step 2 never runs, so the answer is
#         # simply the size of the largest existing island.
#         for i in range(n*n):
#             mx = max(mx, dsu.getSize(dsu.find(i)))

#         return mx

# --------------------------------------------
#                 DFS APPROACH
# --------------------------------------------
# TC: O(N²)
# SC: O(N²)
# --------------------------------------------
class Solution:
    def isValid(self, nrow, ncol):
        return 0 <= nrow < self.n and 0 <= ncol < self.n

    def dfs(self, row, col, island_id, grid):
        """
            returns -> the size of the component
        """
        if not self.isValid(row, col) or grid[row][col] != 1:
            return 0

        size = 1
        grid[row][col] = island_id

        for dr, dc in self.dirs:
            nrow, ncol = row + dr, col + dc
            size += self.dfs(nrow, ncol, island_id, grid)

        return size

    def largestIsland(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.dirs = ((-1, 0), (0,-1), (1,0), (0,1))

        island_size = {}
        island_id = 2 # as 0 and 1 already present

        # label every item and store the size
        for row in range(self.n):
            for col in range(self.n):
                if not grid[row][col]:
                    continue
                size = self.dfs(row, col, island_id, grid)
                island_size[island_id] = size
                island_id += 1

        # edge case when full grid is one island
        ans = max(island_size.values(), default=0)

        # try converting each 0 into 1
        for row in range(self.n):
            for col in range(self.n):
                if grid[row][col]:
                    continue
                
                seen = set()
                total = 1

                for dr, dc in self.dirs:
                    nrow, ncol = dr + row, dc + col

                    if self.isValid(nrow, ncol):
                        parent = grid[nrow][ncol]

                        if parent > 1 and parent not in seen:
                            total += island_size[parent]
                            seen.add(parent)

                ans = max(ans, total)
        
        return ans