class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ## ===============================
        ## APPROACH 1: 
        ## Left - Right Nearest Smaller Calculation and from there get the area for each
        ## ===============================

        # h = len(heights)
        # # left -> Nearest Smaller to left 
        # # right -> Nearest Smaller to right 
        # left, right = [-1] * h, [-1] * h # store indeces
        # stack = [] # store indeces

        # # Nearest Smaller to left 
        # for i in range(h):
        #     while stack and heights[stack[-1]] >= heights[i]:
        #         stack.pop()

        #     left[i] = stack[-1] if stack else -1
        #     stack.append(i)
        
        # # clearing stack to reuse
        # stack = []

        # # Nearest Smaller to right
        # for i in range(h-1, -1, -1):
        #     while stack and heights[stack[-1]] >= heights[i]:
        #         stack.pop()

        #     # for width calculation we need the right to store h not -1
        #     right[i] = stack[-1] if stack else h
        #     stack.append(i)

        # # Nearest Smaller to left and right calculation creates a range that helps in width calculation
        # max_area = 0
        # for i in range(h):
        #     # width calculation
        #     width = right[i] - left[i] - 1
        #     # area calculation
        #     area = heights[i] * width
        #     max_area = max(max_area, area)

        # return max_area

        ## ===============================
        ## APPROACH 2
        ## Instead of calculating Left-Right separatly, doing when popping stack
        ## storing (index, height) in the stack instead
        ## ===============================

        # stack = [] # (index , height)
        # max_area = 0

        # for i, h in enumerate(heights):
        #     start = i
        #     while stack and stack[-1][1] > h:
        #         idx, height = stack.pop()
        #         max_area = max(max_area, height * (i - idx))
        #         start = idx

        #     stack.append((start, h))

        # remaining bars extends to end
        # for i, h in stack:
        #     max_area = max(max_area, h * (len(heights) - i))
        
        # return max_area


        ## ===============================
        ## APPROACH 3
        ## simple but effective
        ## ===============================
        # forces remaining stack elements to pop -> handles rectangles extending to the end.
        heights.append(0)
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                w = i - stack[-1] - 1
                max_area = max(max_area, heights[idx] * w)
            stack.append(i)
        
        heights.pop()
        return max_area


        # NOTE: the most common and easy to remember approach is the first one, cause it is simple monotonic stack in left-right then width calculation. Other two approach are slightly better but overall Time and Space complexity remains same for all O(n) both TC and SC.