import heapq

class Solution:
    # dijkstra
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        # early return
        if grid[m-1][n-1] >= health:
            return False

        dist = [[float('inf')]*n for _ in range(m)]

        # init
        dist[0][0] = grid[0][0]
        pq = [(grid[0][0], 0, 0)] # cost, row, col

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while pq:
            cost, row, col = heapq.heappop(pq)

            # don't go further 
            # if cost became greater then what inside dist 
            # or greater than health
            if cost > dist[row][col] or cost > health:
                continue

            for dr, dc in dirs:
                nrow, ncol = dr + row, dc + col

                if nrow >= 0 and nrow < m and ncol >= 0 and ncol < n: 
                    if cost + grid[nrow][ncol] < dist[nrow][ncol]:
                        dist[nrow][ncol] = cost + grid[nrow][ncol]
                        heapq.heappush(pq, (dist[nrow][ncol], nrow, ncol))

        # final cell health/cost must be 1 or greater
        # so, differnce must be 1 or more
        # i.e. no equal check here
        return dist[m-1][n-1] < health
