class Solution:
    def minAnd2ndMin(self, arr):
        if len(arr) < 2:
            return [-1]
            
        minn, minn2 = float('inf'), float('inf')
        
        if arr[0] > arr[1]: minn, minn2 = arr[1], arr[0]
        else: minn, minn2 = arr[0], arr[1]
        
        for i in range(len(arr)):
            if minn == arr[i]: continue
            elif arr[i] < minn:
                t = minn
                minn = arr[i]
                minn2 = t
            elif arr[i] < minn2:
                minn2 = arr[i]
        
        if minn == minn2: return [-1]
        return [minn, minn2]
            
            