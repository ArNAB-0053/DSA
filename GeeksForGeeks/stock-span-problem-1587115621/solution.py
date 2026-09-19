class Solution:
    def calculateSpan(self, arr):
        stack = [] #(price, span)
        ans = [] # span
        for stock in arr:
            span = 1
            while stack and stack[-1][0] <= stock:
                span += stack.pop()[1]
            ans.append(span)
            stack.append((stock, span))
        return ans