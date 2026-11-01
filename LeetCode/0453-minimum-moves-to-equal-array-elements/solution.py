class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minn, ans = min(nums), 0
        for i in range(len(nums)):
            ans += (nums[i] - minn)
        return ans