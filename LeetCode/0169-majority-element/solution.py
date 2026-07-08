class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm
        # 
        # TC: O(n)
        # SC: O(1)

        # can be done by using dictionary but that would take O(n) time and space complexity
        # where Boyer-Moore Voting Algorithm takes O(n) time but O(1) space complexity

        # Intuition:
        # - Keep a candidate and its count.
        # - If count becomes 0, choose the current number as the new candidate.
        # - If the current number matches the candidate, increase the count.
        # - Otherwise, decrease the count.

        # this works here because
        # - Every different element cancels one occurrence of the candidate.
        # - Since the majority element appears more than n/2 times, it cannot be completely canceled out.
        # - The remaining candidate at the end is the majority element.

        candidate, cnt = None, 0

        for n in nums:
            if cnt == 0:
                candidate = n
                cnt += 1
            elif candidate != n:
                cnt -= 1
            else:
                cnt += 1
        
        return candidate
