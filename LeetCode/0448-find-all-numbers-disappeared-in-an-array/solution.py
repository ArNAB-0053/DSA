class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        t = [0] * (n+1)

        for num in nums:
            if t[num]:
                continue
            t[num] = 1
        
        ans = []
        for i in range(1, n+1):
            if not t[i]:
                ans.append(i)

        return ans