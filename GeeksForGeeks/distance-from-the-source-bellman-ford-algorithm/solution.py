class Solution:
    def bellmanFord(self, V, edges, src):
        INF = 10 ** 8
        dist = [INF] * V
        
        dist[src] = 0
        
        # will run for V-1 time
        for _ in range(V-1):
            # track pass updation true/false
            updated = False
            for u, v, wt in edges:
                if dist[u] != INF and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
                    # if any edge of the pass changes then it'll become true
                    updated = True
            
            # if in that pass nothing being updated
            # means already got the shortest path
            # no need tp go for further checks
            if not updated:
                break
                
        # will run for V th time
        for u, v, wt in edges:
            # if still it is considering new values for dist
            # means cycle present 
            # and return -1
            if dist[u] != INF and dist[u] + wt < dist[v]:
                return [-1]
        
        return dist
        