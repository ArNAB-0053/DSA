import heapq

class Solution:
    # Dijktra 
    # return -> max(dist) # except 0th index
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u, v, wt in times:
            adj[u].append((v, wt))

        dist = [float('inf')] * (n+1)

        # this is to ignore 0th index value
        # because later checking max so it may effect cause all are INF
        # so making it -1 to ignore the max case
        # can remove and later when max checking just do max(dist[1:])
        # it is explicitly said it has node from 1 to n
        dist[0] = -1

        # initials
        dist[k] = 0
        pq = [(0, k)]

        while pq:
            time, node = heapq.heappop(pq)

            if time > dist[node]:
                continue

            for adjNode, t in adj[node]:
                newTime = time + t
                if newTime < dist[adjNode]:
                    dist[adjNode] = newTime
                    heapq.heappush(pq, (newTime, adjNode))

        # if before dist[0] never re-write as -1 then
        # can just do -> ans = max(dist[1:])
        ans = max(dist)
        return ans if ans != float('inf') else -1
