class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        summ = 0
        for i in range(len(nums)):
            s = set()
            cnt = 0
            for j in range(i, len(nums)):
                if nums[j] not in s:
                    cnt += 1
                    s.add(nums[j])
                summ += cnt ** 2
        return summ