class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # TC: O(n)
        # SC: O(n)

        # n = len(nums)
        # t = [0] * (n+1)

        # for num in nums:
        #     if t[num]:
        #         continue
        #     t[num] = 1
        
        # ans = []
        # for i in range(1, n+1):
        #     if not t[i]:
        #         ans.append(i)

        # return ans

        # But we can do the marking in the same array but marking it negative
        # TC: O(n)
        # SC: O(1)
        n = len(nums)

        for num in nums:
            idx = abs(num)-1
            nums[idx] = -abs(nums[idx])
        
        ans = []
        for i, num in enumerate(nums):
            if num > 0:
                ans.append(i+1)

        return ans