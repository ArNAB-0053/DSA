class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1

        while low <= high:
            # mid = (low + high) // 2
            mid = low + ((high - low) // 2)
            if nums[mid] == target:
                return mid

            # means from low to mid is sorted
            if nums[mid] >= nums[low]:
                # checking is target is in range
                # yes : go to left side     | high = mid - 1
                # no : go to right side     | left = mid + 1
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # means from mid to high is sorted
            else:
                # checking is target is in range
                # yes : go to right side    | left = mid + 1
                # no : go to left side      | high = mid - 1
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1   
                    
        return -1
