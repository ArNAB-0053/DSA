class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # -----------------------------------------------
        # Perfectly fine
        # But TC: O(nlogn)
        # and as the constrains are too small we can use conting sort 
        # -----------------------------------------------

        # sorted_nums = sorted(nums)
        # mapp = {}
        # for i, num in enumerate(sorted_nums):
        #     if num not in mapp:
        #         mapp[num] = i

        # ans = []
        # for num in nums:
        #     ans.append(mapp[num])
        
        # return ans

        # -------------------------------------
        #       Counting Sort appraoch
        #       TC: O(n + 101) -> O(n)


        # If the value range were very large (e.g. nums[i] up to 10^9),
        # using a frequency array would be impractical in terms of memory.
        # In that case, the sorting + hashmap approach would be preferred:
        # TC: O(n log n)
        # -------------------------------------

        # Constraints:
        # 2 <= nums.length <= 500
        # 0 <= nums[i] <= 100

        # the element inside nums can be max 100
        # so we can use a constant space for freq and smaller

        # We could also use MAX = max(nums) + 1
        # to allocate only the required size.
        # Here we use 101 directly because the constraint guarantees
        # 0 <= nums[i] <= 100.
        MAX = 101

        # counts frequency
        freq = [0] * MAX
        for num in nums:
            freq[num] += 1

        # prefix array
        smaller = [0] * MAX
        for i in range(1, MAX): 
            smaller[i] = smaller[i-1] + freq[i-1]

        ans = []
        for num in nums:
            ans.append(smaller[num])
        
        return ans