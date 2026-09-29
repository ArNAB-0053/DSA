class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxx, minn = [nums[0]] * n, [nums[-1]] * n

        for i in range(1, n):
            maxx[i] = max(maxx[i-1], nums[i])
        for i in range(n-2, -1, -1):
            minn[i] = min(minn[i + 1], nums[i])

        for i in range(n):
            if maxx[i] - minn[i] <= k:
                return i
        
        return -1