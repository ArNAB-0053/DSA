## Approach 1: Copying matrix into another matrix and just rewrite the value
### Intuition - 
- it asked for inplace we can't return a new array and also as we are going to modify the original matrix the value will change and then if we add, will add wrong value
- so created a copy of main matrix
- then just modifing the values in main matrix from temp

## Approach 2: Transpose + reverse each row
### Intuition -
- getting transpose
- cause transpose means col become rows and rows become column
- then we can just reverse each row to get the ans
- example:
- [[10, 20], [30, 40]] -> transpose -> [[10, 30], [20, 40]]
- reveser each row will give us -> [[30, 10], [40, 20]]
- which is the answer