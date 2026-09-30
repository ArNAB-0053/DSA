class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        minn = [-1] * n 
        minn[-1] = nums[-1]

        for i in range(n-2, -1, -1):
            minn[i] = min(minn[i+1], nums[i])
        
        maxx = nums[0]

        for i in range(n):
            maxx = max(maxx, nums[i])
            if maxx - minn[i] <= k:
                return i

        return -1