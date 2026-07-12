class Solution:
    def maxSubarraySum(self, arr, k):
        i = j = 0
        
        summ = 0
        maxx = 0
        while j < len(arr):
            summ += arr[j]
            if j - i + 1 < k:
                j += 1
            else:
                maxx = max(summ, maxx)
                summ -= arr[i]
                j += 1
                i += 1
            
        return maxx