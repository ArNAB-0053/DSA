class Solution:
    def celebrity(self, mat):
        # Celebrity => A person who known by everyone but doesn't know anyone
        # mat[i][j] = 0 -> i doesn't know j
        # mat[i][j] = 1 -> i knows j
        
        # if there are 'N' person then to become celebrity 'N-1' people 
        # have to know that person
        # so, there can only be one celebrity or none at all
        top, down = 0, len(mat)-1

        # tyring to predict the celebrity by reducing the matrix
        while top < down:
            # if top kowns down then top can never be celebrity
            if mat[top][down] == 1:
                top += 1
            # if down kowns top then down can never be celebrity
            elif mat[down][top] == 1:
                down -= 1
            # if top doesn't know down and down doesn't know top then
            # any of them can't be celebrity
            else:
                top += 1
                down -= 1
        
        # means no celebrity exists
        if top > down:
            return -1
        # as all previous test passes we can say - top == down
        # we are now predicting the top/down can be the celebrity.
        # so we are checking top satisfies the celebrity properties or not.
        # --| as top == down, can use down instead of top as well |--
        for i in range(len(mat)):
            # skip diagonal
            if top == i: 
                continue
            # mat[top][i] -> rows can only have 0s as celeb can't know anyone
            # mat[i][top] -> cols can only have 1s as everyone should know him
            # if that not match then celeb not exists
            elif not (mat[top][i] == 0 and mat[i][top] == 1):
                return -1
        # else top/down is the celeb
        return top