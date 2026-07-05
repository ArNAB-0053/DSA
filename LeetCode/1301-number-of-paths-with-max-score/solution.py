class Solution:
    # helpers
    # for checking the validity of the node
    def isValid(self, i: int, j: int, board: List[str]) -> List[int]:
        # with row and col validation as it can be out of bound, also checking the currect character is 'X' or not
        # cause 'X' means obstacle, so will not go there
        return i >= 0 and i < self.n and j >= 0 and j < self.n and board[i][j] != 'X'
    # coverting str to int
    # if current character isn't 'S' and can be converted to int else returning 0
    def getIntFromChar(self, ch: str):
        return int(ch) if ch != 'S' else 0

    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        self.n = len(board)
        MOD = 10**9 + 7

        # (score, paths with the same score)
        dp = [[(0,0)] * self.n for _ in range(self.n)]
        # inital
        dp[0][0] = (0, 1)

        for i in range(self.n):
            for j in range(self.n):
                # if E means we reached that we already initialize before by making it (0,1)
                # if X means we will not go there cause it is an obstacle 
                # as we initialize all with (0,0) so we good
                if board[i][j] == 'E' or board[i][j] == 'X':
                    continue

                # there are only 3 directions to go - up, left, up-left(diagonal)
                upScore, upPaths = 0, 0
                leftScore, leftPaths = 0, 0
                diagScore, diagPaths = 0, 0
                # current character
                currCh = board[i][j]

                # up -> i-1, j
                if self.isValid(i-1, j, board):
                    score, paths = dp[i-1][j]
                    upScore, upPaths = score, paths
                    if upPaths > 0:
                        upScore += self.getIntFromChar(currCh)

                # left -> i, j
                if self.isValid(i, j-1, board):
                    (score, paths) = dp[i][j-1]
                    leftScore, leftPaths = score, paths
                    if leftPaths > 0:
                        leftScore += self.getIntFromChar(currCh)

                # diagonal / up-left -> i-1, j-1
                if self.isValid(i-1, j-1, board):
                    (score, paths) = dp[i-1][j-1]
                    diagScore, diagPaths = score, paths
                    if diagPaths > 0:
                        diagScore += self.getIntFromChar(currCh)

                bestScore, bestPaths = 0, 0
                # 4 possiblities
                # if all are equal
                if upScore == leftScore and leftScore == diagScore:
                    bestScore = upScore # can be any of them as all are equal
                    bestPaths = upPaths + leftPaths + diagPaths # add the path count
                # if upscore and leftscore are qual but not diagoanl
                elif upScore == leftScore:
                    # initializing
                    bestScore = upScore # can be left as well, both are same
                    bestPaths = upPaths + leftPaths # adding as same best score
                    # up and left are eqaul but what if diag has better score than current bestscore
                    # or what if diag and bestscore same but diagPath > bestPath
                    if diagScore > bestScore or (diagScore == bestScore and diagPaths > bestPaths):
                        bestScore, bestPaths = diagScore, diagPaths
                # if diag and left score are same
                elif diagScore == leftScore:
                    # initializing
                    bestScore = leftScore
                    bestPaths = diagPaths + leftPaths
                    # but what if up has better score than current bestscore
                    # or what if up and best are same but upPaths > bestPaths
                    if upScore > bestScore or (upScore == bestScore and upPaths > bestPaths):
                        bestScore, bestPaths = upScore, upPaths   
                # if none of the above is true  
                else:
                    # initializing with upScore and upPaths 
                    # it will not effect as after that we are checking for left and diag
                    # so initialize can be done using any of up, left or diag
                    # but then after initialization we need to check for other two

                    # as here initializing with up
                    bestScore, bestPaths = upScore, upPaths
                    # so checking for left and diag
                    if leftScore > bestScore or (leftScore == bestScore and leftPaths > bestPaths):
                        bestScore, bestPaths = leftScore, leftPaths
                    if diagScore > bestScore or (diagScore == bestScore and diagPaths > bestPaths):
                        bestScore, bestPaths = diagScore, diagPaths
                # storing the bestScore and bestPath in the dp
                dp[i][j] = (bestScore, bestPaths % MOD) 
        # we know dp[n-1][n-1] has the answer
        # but it has tuple,so converting to list
        return list(dp[self.n-1][self.n-1])