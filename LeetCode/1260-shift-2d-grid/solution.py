class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        # length for 1D array
        n = rows * cols
        # shifting n times means the original 
        # taking the reminder
        k %= n 
        # if k is 0 means even after shifting it will be same as original grid
        if k == 0: return grid
        
        ans = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                # convert the 2D grid index into it's equivalent 1D index
                idx = r * cols + c

                # shift right by k
                # find the new 1D index
                nIdx = (idx + k) % n

                # convert back 1D index to 2D index
                nrow = nIdx // cols
                ncol = nIdx % cols

                # place the current element into it's new position
                ans[nrow][ncol] = grid[r][c]

        return ans