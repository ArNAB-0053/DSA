class Solution:
    # intuition -
    # just traverse through all the nodes and store the minimum
    # as given there will be atlease 1 path between 1 to n means 1 to n will be into a single component always, so don't have to do multi-source DFS.
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n+1)]
        # adjacency list
        for u, v, wt in roads:
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        vis = [0] * (n+1)

        # stors the min weight
        ans = float('inf')
        # normal DFS
        def dfs(node):
            nonlocal ans
            vis[node] = 1
            for adjNode, wt in adj[node]:
                # update with new min wt
                ans = min(ans, wt)
                if not vis[adjNode]:
                    dfs(adjNode)
        # funtion call
        dfs(1)
        return ans
