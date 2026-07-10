class Solution:
	def floydWarshall(self, dist):
	    INF = 10 ** 8
		n = len(dist)
		
        # O(N^3)
		for k in range(n):
    		for i in range(n):
    		    for j in range(n):
    		        if dist[i][k] != INF and dist[k][j] != INF:
        		        dist[i][j] = min(
        		                dist[i][k] + dist[k][j],
        		                dist[i][j]
        		            )
    	
        # Given - it does not contain any negative weight cycles.
        ## if negative cycles exists then - 
        # for i in range(n):
        #     # correct result will have diagonal elements as 0
        #     # if anything comes as lesser than 0 means it has a cycle
            
        #     # because suppose i = 0,
        #     # so, 0 to 0 should always take 0 cost
        #     # but if got any lesser that means 
        #     # we have a cycle which keep on producing min
        #     if dist[i][i] < 0:
        #         # negative cycle exists