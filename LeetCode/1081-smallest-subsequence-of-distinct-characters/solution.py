# Greedy + Monotonic stack

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # stores the last occurance of a character
        # this tells us whether it's safe to remove a character, knowing we can pick it again later
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        visited = [0] * 26
        for i, ch in enumerate(s):
            # as it must be unique
            if visited[ord(ch)-ord('a')]:
                continue
            # if valid stack 
            # [and]
            # topped most element of stack greater than current character, as it asked for samellest
            # (so we can remove those from stack)
            # [and]
            # last of topped most element of greater than current index, means in future there exists same element
            # (so we can overlook it and not add to the answer)

            # this is a greedy step as - we are ignoring (pruning) all other possibilities because we've proved they cannot produce a better answer
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                # so remove from stack mark
                removed = stack.pop()
                # mark the popped element as not visited
                # as removing from stack means we are not concidering it as answer
                # so keeping it as visited is wrong
                visited[ord(removed)-ord('a')] = 0
            # push to stack
            stack.append(ch)
            # mark as visited
            visited[ord(ch)-ord('a')] = 1
        return "".join(stack)