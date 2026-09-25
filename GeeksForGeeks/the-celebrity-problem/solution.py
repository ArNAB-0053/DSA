class Solution:
    def celebrity(self, mat):
        top, down = 0, len(mat)-1
        
        while top < down:
            if mat[top][down] == 1:
                top += 1
            elif mat[down][top] == 1:
                down -= 1
            else:
                top += 1
                down -= 1
                
        if top > down:
            return -1
        
        for i in range(len(mat)):
            if top == i: 
                continue
            elif not (mat[top][i] == 0 and mat[i][top] == 1):
                return -1
                
        return top