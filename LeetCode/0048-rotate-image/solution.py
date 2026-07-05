class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        # -------------------------------------------------------------
        # Copying matrix into another matrix and just rewrite the value
        # -------------------------------------------------------------
        # EASY TO DO AND EASY TO REMEMBER
        # Intuition - 
        # it asked for inplace we can't return a new array and also as we are going to modify the original matrix the value will change and then if we add, will add wrong value
        # so created a copy of main matrix
        # then just modifing the values in main matrix from temp

        # it takes TC - O(n^2) and SC - O(n^2)
        # temp = [row.copy() for row in matrix]

        # for r in range(n):
        #     for c in range(n):
        #         # observation - 
        #         # this -> will become 
        #         # 0, 0 -> 2, 0
        #         # 0, 1 -> 1, 0
        #         # 0, 2 -> 0, 0
        #         matrix[r][c] = temp[n-c-1][r]
        

        # Better solution
        # -----------------------------------------------------
        #            Using TRANSPOSE + REVERSE ROW
        # -----------------------------------------------------
        # using or getting transpose
        # cause transpose means col become rows and rows become column
        # then we can just reverse each row to get the ans
        # example:
        # [[10, 20], [30, 40]] -> transpose -> [[10, 30], [20, 40]]
        # reveser each row will give us -> [[30, 10], [40, 20]]
        # which is the answer

        # it will take TC -> O(n^2) but SC -> O(1)

        for r in range(n):
            for c in range(r+1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for row in matrix:
            row.reverse()