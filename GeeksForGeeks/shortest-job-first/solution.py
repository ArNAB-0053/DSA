class Solution:
    def solve(self, bt):
        n = len(bt)
        bt.sort()
        
        wt = [0] * n
        for i in range(1, n):
            wt[i] = wt[i-1] + bt[i-1]
            
        return sum(wt) // n