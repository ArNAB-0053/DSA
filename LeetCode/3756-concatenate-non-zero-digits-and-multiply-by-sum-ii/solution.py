class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        m = len(s)

        # digit sum
        digiSum = [0] * m
        digiSum[0] = int(s[0])
        for i in range(1, m):
            digiSum[i] = digiSum[i-1] + int(s[i])
        
        # number upto
        numUpto = [0] * m
        numUpto[0] = int(s[0])
        for i in range(1, m):
            if s[i] == '0':
                numUpto[i] = numUpto[i-1]
            else:
                numUpto[i] = (numUpto[i-1] * 10 + int(s[i])) % MOD

        # power
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # non-zero count
        nonZero = [0] * m
        nonZero[0] = 1 if s[0] != '0' else 0
        for i in range(1, m):
            if s[i] != '0':
                nonZero[i] = nonZero[i-1] + 1
            else:
                nonZero[i] = nonZero[i-1]
        
        # final answer
        ans = []
        for l, r in queries:
            if l == 0:
                summ = digiSum[r]
                x = numUpto[r]
            else:
                summ = digiSum[r] - digiSum[l-1]
                k = nonZero[r] - nonZero[l-1]
                x = (numUpto[r] - (numUpto[l-1] * pow10[k] % MOD) + MOD) % MOD
            
            ans.append((summ * x) % MOD)

        return ans