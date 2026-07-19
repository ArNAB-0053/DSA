class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        n = len(nums)
        start, end = float('inf'), 0

        # left search
        low, high = 0, n-1
        # this is to find the left most index of target
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                start = mid
                high = mid-1 # ensures it search to left
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1

        # BASE CASES
        # if start is INF means, target not present in nums
        if start == float('inf'):
            return [-1, -1]
        # - if start is the last index
        # - if next element of start not target 
        # - means for both cases only one target present 
        # - and start is both start and end or first and last
        if start == n-1:
            return [start, start]
        if nums[start + 1] != target:
            return [start, start]

        # right search
        low, high = 0, n-1
        # this is to find the last or end index for target
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                end = mid
                low = mid + 1 # ensures it search to the right
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        
        return [start, end]