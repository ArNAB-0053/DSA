class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxx, ans = max(nums), 0
        for i in range(len(nums)):
            ans += (maxx - nums[i])
        return ans