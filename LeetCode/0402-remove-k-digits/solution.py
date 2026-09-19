class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        # base case - when have to remove all the items
        if n <= k: return "0"

        # monotonic stack
        stack = []
        for digit in num:
            # only pop until pop count reached k
            # NOTE:
            # avoiding int() conversions as it works with characters too means -
            # Both of these work:
            # - int(stack[-1]) > int(digit)
            # - stack[-1] > digit
            # Since '0' < '1' < ... < '9', digit characters can be compared directly.
            # (I didn't know that)
            while stack and stack[-1] > digit and k > 0:
                stack.pop()
                k -= 1
            # inserting string
            stack.append(digit)

        # EDGE CASE
        # k may still be > 0 if the number is already monotonic increasing
        # and there will not be any chance of k > len(stack) as we previously ensure n > k.
        while k > 0:
            stack.pop()
            k -= 1

        # removing 0s from the front
        i = 0
        while i < len(stack) and stack[i] == "0":
            i += 1
        # means only 0s are present in the stack
        if i == len(stack):
            return "0"
        # joining the items to create answer
        return "".join(stack[i:])