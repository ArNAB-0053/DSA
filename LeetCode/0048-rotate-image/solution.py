class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Intuition - 
        # it asked for inplace we can't return a new array and also as we are going to modify the original matrix the value will change and then if we add, will add wrong value
        # so created a copy of main matrix
        # then just modifing the values in main matrix from temp
        n = len(matrix)
        temp = [row.copy() for row in matrix]

        for r in range(n):
            for c in range(n):
                # observation - 
                # this -> will become 
                # 0, 0 -> 2, 0
                # 0, 1 -> 1, 0
                # 0, 2 -> 0, 0
                matrix[r][c] = temp[n-c-1][r]
        
        