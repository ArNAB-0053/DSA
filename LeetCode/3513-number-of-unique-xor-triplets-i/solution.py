class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        # For n >= 3, the number of unique XOR triplet values is the smallest power of 2 strictly greater than n.
        # XOR cannot create a new higher bit: if all numbers fit within k bits,
        # their XOR will also fit within k bits, giving values in [0, 2^k - 1].
        # n = 1 and n = 2 are special cases, where the answer is n.
        n = len(nums)
        
        if n <= 2:
            return n

        ans = 1 # 2^0
        while ans <= n:
            ans *= 2

        return ans