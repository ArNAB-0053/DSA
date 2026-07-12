class Solution:
    def maxChildren(self, greed, cookie):
        greed.sort()
        cookie.sort()
        
        gi = ci = 0
        
        while gi < len(greed) and ci < len(cookie):
            if greed[gi] <= cookie[ci]:
                gi += 1
            ci += 1
        
        return gi