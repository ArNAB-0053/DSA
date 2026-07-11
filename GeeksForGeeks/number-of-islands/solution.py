from typing import List

class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)

        if pa == pb:
            return False # tiny optimization - avoids extra find() calls

        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa

        self.parents[pb] = pa
        self.size[pa] += self.size[pb]
        
        # as returning false there need to return true if all works
        return True

class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        dsu = DSU(rows * cols)
        # 4 directions
        dirs = ((-1, 0), (0,-1), (1,0), (0,1))
        
        # visited array
        vis = [[0] * cols for _ in range(rows)]
        ans = [] # stores answer
        cnt = 0 # counts
        for row, col in operators:
            # if already visited 
            # then append the count into answer
            # and go to next
            if vis[row][col]:
                ans.append(cnt)
                continue
            
            vis[row][col] = 1
            
            # assume all the time that current element is a new component
            # so increase the count by 1
            cnt += 1
            
            # delta row, delta col
            for dr, dc in dirs:
                nrow, ncol = dr + row, dc + col
                
                # neighbors validity check + if only already visited
                # then create the connection
                # else just skip this phase
                if nrow >= 0 and nrow < rows and ncol >= 0 and ncol < cols and vis[nrow][ncol]:
                    # formula : index = row * cols + col
                    node = row * cols + col
                    adjNode = nrow * cols + ncol
                    
                    # checks the neighbors having same representative or not
                    # if yes then no point of creating connection again
                    # but if not then create connection
                    # and as there is been a new connection means 
                    # our assumption previously of current as new component was wrong
                    # so decrease the count
                    if dsu.find(node) != dsu.find(adjNode):
                        if dsu.union(node, adjNode):
                            cnt -= 1
                    
            ans.append(cnt)
            
        return ans
                    
                    