class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ## BRUTE FORCE || O(n.m) - (Works on this Constraints)
        # cnt = 0
        # for i in range(len(arr1)):
        #     for j in range(len(arr2)):
        #         if abs(arr1[i] - arr2[j]) <= d:
        #             cnt += 1
        #             break
        
        # return len(arr1) - cnt

        ## TWO POINTER + BINARY SEARCH || O(n.mlogm)
        arr2.sort()
        cnt = 0 # counts not far elements
        for x in arr1:
            l, r = 0, len(arr2)n - 1
            while l <= r:
                mid = (l + r) // 2

                if abs(arr2[mid] - x) <= d: 
                    cnt += 1
                    break
                
                if x - d < arr2[mid]: r = mid - 1
                else: l = mid + 1

        return len(arr1) - cnt

