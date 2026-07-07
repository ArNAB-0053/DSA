import heapq

class Solution:
    # Dijktra + maxheap
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for _ in range(n)]

        for i, (u, v) in enumerate(edges):
            adj[u].append((v, succProb[i]))
            adj[v].append((u, succProb[i]))

        dist = [-1.0] * n
        pq = [(-1.0, start_node)]
        dist[start_node] = 1.0

        while pq:
            prob, node = heapq.heappop(pq)
            prob = -prob

            if dist[node] > prob:
                continue
            
            if node == end_node:
                return prob

            for adjNode, sProb in adj[node]:
                newProb = prob * sProb

                if newProb > dist[adjNode]:
                    dist[adjNode] = newProb
                    heapq.heappush(pq, (-newProb, adjNode))

        return 0