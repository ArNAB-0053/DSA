class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        stack = []
        m = max(target)
        
        i, j = 1,0
        while i < n+1:
            if i > m:
                break
            stack.append(i)
            ans.append("Push")

            if stack[-1] != target[j]:
                stack.pop()
                ans.append("Pop")
            else:
                j += 1
                
            i += 1

        return ans