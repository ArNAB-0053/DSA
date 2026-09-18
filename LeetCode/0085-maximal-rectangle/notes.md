**this question is extend version of "Largest Rectangle in Histogram"**-> https://leetcode.com/problems/largest-rectangle-in-histogram/description

## Intuition
- From `Largest Rectangle in Histogram` question, we know how to get largest reactangle for an array with heights.
- In this problem as it is given a matrix we can treat each row as an array that holds the heights, and ***to know the height we can add continuous 1's in a column***.
- Then we can just pass that to the `largestRentangle()` function and store the max out from that.

### What I meant by *"to know the height we can add continuous 1's in a column"*
```text
Input:
[
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]

After calculating consecutive heights:
[
    [1, 0, 1, 0, 0],
    [2, 0, 2, 1, 1],
    [3, 1, 3, 2, 2],
    [4, 0, 0, 3, 0]
]

 >> the columns being added to get the height of the currect row, 
 and if we encounter 0, the height will be 0 and the sum will get 
 cut of and start again.
```

> NOTE: 
I am appling PSE + NSE approach, as I think that I'll remember most of the time rather than shorter versions