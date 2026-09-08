class Solution:
	def prevSmaller(self, arr):
	    n = len(arr)
        ans = [-1] * n

        stack = []

        for i, num in enumerate(arr):
            while stack and stack[-1] >= num:
                stack.pop()
            if stack and num > stack[-1]:
                ans[i] = stack[-1]
            stack.append(num)

        return ans