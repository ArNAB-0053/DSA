class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        # s = "10203004" -> will follow this example for each array
        MOD = 10 ** 9 + 7

        m = len(s)
        # Prefix sum of digits
        # digiSum[i] = sum of all digits from s[0] to s[i]
        # e. g. [1,1,3,3,6,6,6,10]
        digiSum = [0] * m
        digiSum[0] = int(s[0])
        for i in range(1, m):
            digiSum[i] = digiSum[i-1] + int(s[i])
        
        # Prefix concatenation value of non-zero digits
        # numUpto[i] = number formed by concatenating all non-zero digits from s[0] to s[i] (stored modulo MOD)
        # e. g. [1,1,12,12,123,123,123,1234]
        numUpto = [0] * m
        numUpto[0] = int(s[0])
        for i in range(1, m):
            if s[i] == '0':
                numUpto[i] = numUpto[i-1]
            else:
                numUpto[i] = (numUpto[i-1] * 10 + int(s[i])) % MOD

        # pow10[i] = 10^i mod MOD
        # Used to remove the contribution of the left prefix when extracting a range concatenation
        # e.g. [1,10,100,1000, ...]
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # Prefix count of non-zero digits
        # nonZero[i] = number of non-zero digits in s[0:i+1]
        # e.g. [1,1,2,2,3,3,3,4]
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
                # Number of non-zero digits in the range
                k = nonZero[r] - nonZero[l-1]
                # Remove left prefix contribution
                x = (numUpto[r] - (numUpto[l-1] * pow10[k] % MOD) + MOD) % MOD

            # EXAMPLE WORKFLOW - 
            # suppose s = "10203004", queries = [[0,7],[1,3],[4,6]]
            # we taking a simple range (1,3)

            ## --- THE VALUES WRITTEN ON EACH STEPS --- ##
            # l != 0 so it will go to else -
            # summ = digiSum[3] - digiSum[0] = 3-1 = 2
            # k = nonZero[3] - nonZero[0] = 2-1 = 1
            # x = (numUpto[3] - (numUpto[0] * pow10[1] % MOD) + MOD) % MOD 
            #   = 12 - (1 * 10) ## this is a samll no., no point of MOD
            #   = 2

            # summ * x = 2 * 2 = 4
            
            ans.append((summ * x) % MOD)

        return ans