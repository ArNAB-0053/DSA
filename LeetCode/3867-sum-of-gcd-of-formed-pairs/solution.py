import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = []
        length, largest = 0, 0
        for num in nums:
            largest = max(largest, num)
            gcd = math.gcd(num, largest)
            prefix_gcd.append(gcd)
            length += 1

        prefix_gcd.sort()
        i, j = 0, len(prefix_gcd) - 1
        ans = 0
        while i < j:
            ans += math.gcd(prefix_gcd[i], prefix_gcd[j])
            i += 1
            j -= 1
        
        return ans