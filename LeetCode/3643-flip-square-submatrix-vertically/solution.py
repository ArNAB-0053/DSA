class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        if y + k > len(grid[0]) or k == 1:
            return grid
        
        l, r = x, x + k -1

        while l < r:
            left, right = grid[l], grid[r]
            for i in range(y, y+k):
                left[i], right[i] = right[i], left[i]
            l += 1
            r -= 1
        
        return grid