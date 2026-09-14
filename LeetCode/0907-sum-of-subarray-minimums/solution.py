class Solution:
    # If values are equal, we don't want both of them to count the same subarray. So we keep equal on one and remove equal on the other.

    # NSE uses >=, so equal elements are removed from the stack.
    # PESE uses >, so an equal element is allowed to remain.
    
    # Next Smaller Element
    def findNSE(self, arr: List[int]) -> int:
        stack = []
        NSE = [-1] * self.n

        for i in range(self.n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            NSE[i] = stack[-1] if stack else self.n
            stack.append(i)

        return NSE

    # Previous Equal or Smaller Element
    def findPESE(self, arr: List[int]) -> int:
        stack = []
        PESE = [-1] * self.n

        for i in range(self.n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack: PESE[i] = stack[-1]
            stack.append(i)

        return PESE

    def sumSubarrayMins(self, arr: List[int]) -> int:
        self.n = len(arr)
        NSE = self.findNSE(arr)
        PESE = self.findPESE(arr)
        total = 0
        MOD = 10 ** 9 + 7

        for i in range(self.n):
            left = i - PESE[i]
            right = NSE[i] - i

            total = (total + (left * right * arr[i]) % MOD ) % MOD

        return total % MOD