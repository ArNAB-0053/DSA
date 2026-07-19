class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i
        
        stack, visited = [], [0] * 26

        for i, ch in enumerate(s):
            if visited[ord(ch)-ord('a')] == 1:
                continue
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                removed = stack.pop()
                visited[ord(removed)-ord('a')] = 0
            stack.append(ch)
            visited[ord(ch)-ord('a')] = 1

        return "".join(stack)