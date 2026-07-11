# -----------------------------------------------------------
#                   DSU APPROACH
# -----------------------------------------------------------

# TC: O((V + E)·α(V)) ≈ O(V + E)
# SC: O(V)

# class DSU:
#     def __init__(self, n):
#         self.parents = list(range(n))
#         self.size = [1] * n
#         # keeps the edges count
#         self.edges = [0] * n
#         # to make sure we don't have to measure the length every time
#         # and to get length in linear time
#         self.length = n 

#     def find(self, x):
#         if self.parents[x] != x:
#             self.parents[x] = self.find(self.parents[x])
#         return self.parents[x]

#     def union(self, a, b):
#         pa, pb = self.find(a), self.find(b)

#         if pa == pb:
#             # if pa and pb already have same root parent
#             # means a, b are connected
#             # so adding +1 to the edges
#             self.edges[pa] += 1
#             return

#         if self.size[pa] < self.size[pb]:
#             pa, pb = pb, pa

#         self.parents[pb] = pa
#         self.size[pa] += self.size[pb]
#         # if any new smaller component is being connected 
#         # means the root parent edge will become the edges count of smaller component + 1 extra edge that creates connection between them 
#         self.edges[pa] += self.edges[pb] + 1

#     def getCompleteComponents(self):
#         """
#             returns: no. of complete connected components
#         """
#         ans = 0

#         for i in range(self.length):
#             if self.find(i) == i:
#                 nodes = self.size[i] # size keeping tracks of vertices count

#                 # for complete graph
#                 # E = n * (n-1) / 2
#                 # E: no. of edges
#                 # n: no. of vertices
#                 if self.edges[i] == nodes * (nodes - 1) // 2:
#                     ans += 1

#         return ans


# class Solution:
#     def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
#         dsu = DSU(n)

#         for u, v in edges:
#             dsu.union(u, v)

#         return dsu.getCompleteComponents()


# ----------------------------------------------------------
#                       BFS/DFS APPROACH
# ----------------------------------------------------------

# Intuition : 
# - Just go for each connected component 
# - count the number of edges and vertices
# - if edges = vertices * (vertices - 1) // 2 then increase the count by 1

# TC: O(V + E)
# SC: O(V + E)
class Solution:
    def dfs(self, node, adj, vis ):
        vis[node] = 1

        # vertices count
        nodes = 1
        # degree count
        degree_sum = len(adj[node])

        for it in adj[node]:
            if not vis[it]:
                n, d = self.dfs(it, adj, vis)
                # nodes and degree updation
                nodes += n
                degree_sum += d

        return nodes, degree_sum

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = [0] * n
        ans = 0
        for i in range(n):
            if not vis[i]:
                nodes, degree_sum = self.dfs(i, adj, vis)
                # as it is undirected graph
                # total edges = degree_sum // 2
                edges = degree_sum // 2
                if edges == nodes * (nodes-1) // 2:
                    ans += 1

        return ans


        
