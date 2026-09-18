class Solution:
    ## this question is extend version of "Largest Rectangle in Histogram" -> https://leetcode.com/problems/largest-rectangle-in-histogram/description

    ## Intuition
    # - from "Largest Rectangle in Histogram" question, we know how to get largest reactangle for an array with heights
    # - in this problem as it is given a matrix we can treat each row as an array that holds the heights, and to know the height we can add continuous 1's in a col.
    # - then we can just pass that to the "LargestRentangle" function and store the max out from that.

    ## NOTE: 
    # I am appling PSE + NSE approach, as I think that I'll remember most of the time rather than shorter versions
    def largestRectangle(self, arr, n):
        # left -> PSE | right -> NSE
        # all stores indexes
        left, right = [-1] * n, [n] * n
        stack = []

        # PSE
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack: left[i] = stack[-1]
            stack.append(i)

        stack=[]
        
        # NSE
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack: right[i] = stack[-1]
            stack.append(i)
        
        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            max_area = max(max_area, width * arr[i])

        return max_area

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        n, m = len(matrix), len(matrix[0])

        # initializing with 0
        heights = [ [0] * m for _ in range(n)]

        # doing column-row loop to get the sum of consecutive 1s in that column upto currect row
        # building histogram heights for each row:
        # heights[i][j] = number of consecutive 1s ending at (i, j)
        for j in range(m):
            summ = 0
            for i in range(n):
                summ += int(matrix[i][j])
                if matrix[i][j] == "0": summ = 0
                heights[i][j] = summ

        print(heights)
        
        # finding actual answer
        max_rectangle = 0
        for arr in heights:
            max_rectangle = max(max_rectangle, self.largestRectangle(arr, m)) # m = len(arr)
        
        return max_rectangle