class Solution:
    # It is same as `https://www.geeksforgeeks.org/problems/sum-of-subarray-minimum/1` but 
    # there we used Previous Smaller and Next Smaller element where here it will be -
    # Previous Greater and Next Greater element.
    # Everything else will be same - just these two changes
    
    # If values are equal, we don't want both of them to count the same subarray. 
    # So we keep equal on one and remove equal on the other.

    # NGE uses >=, so equal elements are removed from the stack.
    # PEGE uses >, so an equal element is allowed to remain.

    # Next Greater Element
    def findNGE(self, arr):
        stack = []
        NGE = [-1] * self.n

        for i in range(self.n-1, -1, -1):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            NGE[i] = stack[-1] if stack else self.n
            stack.append(i)

        return NGE

    # Previous Equal or Greater Element
    def findPEGE(self, arr):
        stack = []
        PEGE = [-1] * self.n

        for i in range(self.n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if stack: PEGE[i] = stack[-1]
            stack.append(i)

        return PEGE
        
    def sumOfMax(self, arr):
        self.n = len(arr)
        NGE = self.findNGE(arr)
        PEGE = self.findPEGE(arr)
        total = 0
        MOD = 10 ** 9 + 7

        for i in range(self.n):
            left = i - PEGE[i]
            right = NGE[i] - i

            total += (left * right * arr[i]) 

        return total
        