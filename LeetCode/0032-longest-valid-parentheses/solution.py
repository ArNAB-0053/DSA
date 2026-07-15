class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxLen = 0
        for i,p in enumerate(s):
            if p == "(":
                stack.append(i)
            else:
                stack.pop()
                # if stack is empty and p is ")"
                if not stack:
                    stack.append(i)
                else:
                    maxLen = max(maxLen, i - stack[-1])

        return maxLen