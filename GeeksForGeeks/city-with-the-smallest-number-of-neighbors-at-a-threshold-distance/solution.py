from typing import List
import heapq

class Solution:
    ## done using FLOYD WARSHELL
    ## takes O(n^3) for creating distance matrix
    
    # def findCity(self, n : int, m : int, edges : List[List[int]], distanceThreshold : int) -> int:
        # INF = float('inf')
        
        # dist = [[INF] * n for _ in range(n)]
        
        # # creating adj matrix
        # for u, v, wt in edges:
        #     dist[u][v] = wt
        #     dist[v][u] = wt
            
        # # all diagonal is 0
        # for i in range(n):
        #     dist[i][i] = 0
        
        # # the distance matrix
        # # O(n^3)
        # for k in range(n):
        #     for i in range(n):
        #         for j in range(n):
        #             if dist[i][k] != INF and dist[k][j] != INF:
        #                 dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                        
        # cntMax = n+1
        # cityNo = -1
        
        # # counting for each -
        # # is the no. of items that are lesser than the threshold
        # # and storing min to cntMax
        # # and the max of row which is the current city to cityNo
        # for r in range(n):
        #     cnt = 0
        #     for c in range(n):
        #         # r -> row = current city
        #         # c -> col = adj city
                
        #         # if not diagonal - cause there is no point of counting that
        #         # and lesser than threshold
        #         if r != c and dist[r][c] <= distanceThreshold:
        #             cnt += 1
        #     if cnt <= cntMax:
        #         cntMax = cnt
        #         cityNo = r
                
        # return cityNo
    
    ## USING DIHKSTRA to all vertex
    
    # take O(mlogn) for single source tp destination
    # will take O(mnlogn) for all sources to destination
    # which is still lower than n^3
    def dijkstra(self, n: int, src: int, adj: any):
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0
        
        pq = [(0, src)]
        
        while pq:
            dis, node = heapq.heappop(pq)
            
            if dis > dist[node]:
                continue
            
            for adjNode, wt in adj[node]:
                newDist = dis + wt
                
                if newDist < dist[adjNode]:
                    dist[adjNode] = newDist
                    heapq.heappush(pq, (newDist, adjNode))
                    
        return dist
                
    
    def findCity(self, n : int, m : int, edges : List[List[int]], distanceThreshold : int) -> int:
        adj = [[] for _ in range(n)]
        
        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))
            
        cntMax = n+1
        cityNo = -1
        
        for city in range(n):
            dist = self.dijkstra(n, city, adj)
            
            cnt = 0
            
            for d in dist:
                if d <= distanceThreshold:
                    cnt += 1
                    
            if cnt <= cntMax:
                cntMax = cnt
                cityNo = city
        
        return cityNo
                
        
        
        
        
        