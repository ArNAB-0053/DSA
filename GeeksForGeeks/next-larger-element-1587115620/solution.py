class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        stack = []
        ans = [-1] * n
        
        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            
            ans[i] = stack[-1] if stack else -1
            stack.append(arr[i])
            
        return ans