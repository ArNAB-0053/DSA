class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        # 0's count upto a 1
        zeros = []
        # cntOnes - count of 1s present in the string
        i, cntOnes = 0, 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                zeros.append(i-start)
            else:
                cntOnes += 1
                i += 1
        maxPairs = 0

        if len(zeros) < 2:
            return cntOnes

        # get the max pairs
        for i in range(1, len(zeros)):
            maxPairs = max(maxPairs, zeros[i-1] + zeros[i])
        return maxPairs + cntOnes