class Solution:
    ## this question is extend version of "Largest Rectangle in Histogram" 
    # -> https://leetcode.com/problems/largest-rectangle-in-histogram/description

    ## Intuition
    # - from "Largest Rectangle in Histogram" question, we know how to get largest 
    # reactangle for an array with heights
    # - in this problem as it is given a matrix we can treat each row as an array 
    # that holds the heights, and to know the height we can add continuous 1's in a col.
    # - then we can just pass that to the "LargetRentangle" function and store the max 
    # out from that.

    ## NOTE: 
    # I am appling PSE + NSE approach, as I think that I'll remember most of the time 
    # rather than shorter versions
    def longestRectangle(self, heights, h):
        # left -> PSE | right -> NSE | (stores indexes)
        left, right, stack = [-1] * h, [h] * h, []
        
        # PSE
        for i in range(h):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack: left[i] = stack[-1]
            stack.append(i)
            
        # reusing same stack
        stack=[]
        
        # NSE
        for i in range(h-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack: right[i] = stack[-1]
            stack.append(i)
            
        max_area = 0
        for i in range(h):
            width = right[i] - left[i] - 1
            max_area = max(max_area, heights[i] * width)
            
        return max_area
            
    def maxArea(self, mat):
        rows, cols = len(mat), len(mat[0])
        
        # initializing with 0
        height_matrix = [[0]  * cols for _ in range(rows)]
        
        # calculating height matrix
        # height_matrix[i][j] = number of consecutive 1s in (i,j)
        # doing column-row loop to get the sum of consecutive 1s in that column upto currect row
        for j in range(cols):
            summ = 0
            for i in range(rows):
                summ += mat[i][j]
                if mat[i][j] == 0: summ = 0
                height_matrix[i][j] = summ
                
        
        # answer calculation
        max_area = 0
        for heights in height_matrix:
            max_area = max(max_area, self.longestRectangle(heights, cols)) # cols = len(heights)
        
        return max_area
                
                