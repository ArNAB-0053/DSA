class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # TC: O(nlogn) || SC: O(1)
        # Output Array Space: O(k)
        # nums.sort()
        # ans = []

        # # i, j = 0, 1
        # # while j < len(nums):
        # #     # mis = nums[j] - nums[i] - 1
        # #     # for n in range(1, mis+1):
        # #     #     ans.append(nums[i]+n)

        # #     for x in range(nums[i]+1, nums[j]):
        # #         ans.append(x)

        # #     i += 1
        # #     j += 1

        # for i in range(len(nums)-1):
        #     for x in range(nums[i]+1, nums[i+1]):
        #         ans.append(x)
        
        # return ans

        ## BETTER TC
        ## Based on Contraints we can solve it in O(n) by introducting an extra array
        # General:
        # TC: O(n + max(nums))
        # Auxiliary SC: O(max(nums))

        # Since nums[i] <= 100:
        # TC: O(n)
        # Auxiliary SC: O(1)
        # Output Space: O(k)
        mn, mx = 101, 0 # I can take mn as 101 as Constraints -> 1 <= nums[i] <= 100
        exists = [False] * 101 # constant space

        for n in nums:
            exists[n-1] = True
            mn = min(n, mn)
            mx = max(n, mx)

        ans = []
        for i in range(mn, mx):
            if not exists[i]:
                ans.append(i+1)
        
        return ans

