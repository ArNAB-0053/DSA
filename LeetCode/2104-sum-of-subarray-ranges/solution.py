class Solution:
    ## uses the concept of sum of subarray minimums and sum of subarray maximums
    ## ans = sum of subarray maximums - sum of subarray minimums
    ## can visit - 
    ## sum of subarray minimums : 
    # - https://leetcode.com/problems/sum-of-subarray-minimums/
    # - https://www.geeksforgeeks.org/problems/sum-of-subarray-minimum/1
    ## sum of subarray maximums : 
    # - https://www.geeksforgeeks.org/problems/sum-of-max-of-subarrays/1
    

    # Next Smaller Element
    def findNSE(self, arr: List[int]) -> int:
        stack = []
        NSE = [-1] * self.n

        for i in range(self.n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            NSE[i] = stack[-1] if stack else self.n
            stack.append(i)

        return NSE

    # Previous Equal or Smaller Element
    def findPESE(self, arr: List[int]) -> int:
        stack = []
        PESE = [-1] * self.n

        for i in range(self.n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack: PESE[i] = stack[-1]
            stack.append(i)

        return PESE

    # Next Greater Element
    def findNGE(self, arr: List[int]) -> int:
        stack = []
        NGE = [-1] * self.n

        for i in range(self.n-1, -1, -1):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            NGE[i] = stack[-1] if stack else self.n
            stack.append(i)

        return NGE

    # Previous Equal or Greater Element
    def findPEGE(self, arr: List[int]) -> int:
        stack = []
        PEGE = [-1] * self.n

        for i in range(self.n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if stack: PEGE[i] = stack[-1]
            stack.append(i)

        return PEGE

    def subArrayRanges(self, nums: List[int]) -> int:
        self.n = len(nums)
        # Smaller elements
        NSE = self.findNSE(nums)
        PESE = self.findPESE(nums)
        # greater elements
        NGE = self.findNGE(nums)
        PEGE = self.findPEGE(nums)
        # answer
        total_min = total_max = 0

        for i in range(self.n):
            left_min = i - PESE[i]
            right_min = NSE[i] - i

            left_max = i - PEGE[i]
            right_max = NGE[i] - i

            total_min += (left_min * right_min * nums[i])
            total_max += (left_max * right_max * nums[i])

        return total_max - total_min