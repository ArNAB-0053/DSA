class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        # TC: n^2 + n + B (B = 2048)
        # n = len(nums)
        # unq = set()

        # for i in range(n):
        #     for j in range(i, n):
        #         unq.add(nums[i] ^ nums[j])

        # ans = set()
        # for num in nums:
        #     for ele in unq:
        #         ans.add(ele ^ num)

        # return len(ans)

        # TC: n * B (B = 2048)
        poss = {0}

        for _ in range(3):
            nxt = set()
            for xor in poss:
                for num in nums:
                    nxt.add(xor ^ num)
            poss = nxt

        return len(poss)