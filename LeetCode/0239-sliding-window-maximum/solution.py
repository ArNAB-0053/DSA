from collections import deque
class Solution:
    ## Monotonic Queue
    ## monotonic decreasing ordered deque
    ## deque -> appends element from back(right) and removes from front(left)
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        ans = []
        for i in range(len(nums)):
            # remove elements outside window
            if dq and dq[0] <= i - k:
                dq.popleft()
            # Previous Greater Element
            # pop when right of dq has smaller or equal element
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            # append index to dq
            dq.append(i)
            # ignore until you reach window length
            if i < k-1: 
                continue
            # append to answer
            ans.append(nums[dq[0]])

        return ans
            