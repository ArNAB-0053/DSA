class Solution:
    ## Monotonic Stack
    def nextGreater(self, arr):
        # code here
        n = len(arr)
        stack, ans = [], [-1] * n
        
        # as this is like circular array-
        # the extra loop ensures that potential NGE candidates from the 
        # wrapped-around portion of the circular array are present in the 
        # stack when we calculate the answers.
        for i in range(n-1,-1,-1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            stack.append(arr[i])
        
        # this loop is to get the answer
        for i in range(n-1,-1,-1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            ans[i] = stack[-1] if stack else -1
            stack.append(arr[i])
        
        return ans