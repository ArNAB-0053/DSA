# -------------------------------------
#       USING PRIM'S ALGORITHM 
# -------------------------------------
# TC: O(E log V)

# import heapq
# class Solution:
#     def spanningTree(self, V, edges):
#         vis = [0] * V
        
#         adj = [[] for _ in range(V)]
        
#         # adjList
#         for u, v, wt in edges:
#             adj[u].append((v, wt))
#             adj[v].append((u, wt))
        
#         ## IF IT HAS ASKED FOR MST and SUM
#         # pq = [(0, 0, -1)] # wt, src, parent
        
#         # mst = [] # (weight, node, parent)
#         # summ = 0
        
#         # while pq:
#         #     wt, node, parent = heapq.heappop(pq)
            
#         #     if vis[node]:
#         #         continue
            
#         #     vis[node] = 1
#         #     summ += wt
#         #     mst.append((wt, node, parent))
            
#         #     for adjNode, adjwt in adj[node]:
#         #         if not vis[adjNode]:
#         #             heapq.heappush(pq, (adjwt, adjNode, node))
                    
                    
#         ## return the mst and summ
#         ## but mst now is a list of (weight, node, parent)
#         ## we will be needing to create a graph if asked for
        
        
#         # actual answer for this question
#         pq = [(0, 0)] # wt, src
        
#         summ = 0
        
#         while pq:
#             wt, node = heapq.heappop(pq)
            
#             if vis[node]:
#                 continue
            
#             # only update node as visited after it comes from the pq
#             # initially all will be 0
#             vis[node] = 1
#             # update the sum
#             summ += wt
            
#             for adjNode, edW in adj[node]:
#                 if not vis[adjNode]:
#                     heapq.heappush(pq, (edW, adjNode))
                    
#         return summ


# -------------------------------------
#       USING KRUSKAL'S ALGORITH
#      (Disjoint Set Union - DSU)
# -------------------------------------

# TC: O(E log E)

class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1]*n
    
    # Find the representative (root) of each component
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
            
        return self.parents[x]
        
    # merges smaller component to larger component
    def union(self, a, b):
        # finding the root parent
        pa, pb = self.find(a), self.find(b)
        
        if pa == pb:
            return False
        
        # always smaller one merges to larger one
#       # from here we are ensuring pa always be bigger
        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa
            
        # merging pb to pa
        self.parents[pb] = pa
        # increasing the size as well
        self.size[pa] += self.size[pb]
        
        return True
        
    # returns is u and v are inside same component or not
    # basically truthness of u and v are connected
    def isConnected(self, u, v):
        return self.find(u) == self.find(v)

class Solution:
    def spanningTree(self, V, edges):
        # calling upon the DSU
        dsu = DSU(V)
        
        # as only it asked for samll weighted sum
        mstWt = 0
        
        # sorting edges based on the weight
        edges.sort(key=lambda x:x[2])
        
        # the main loop
        for u, v, wt in edges:
            # if u and v are not connected
            # then only connect them and update the weight
            
            # if u and v are connected then
            # there is no point of creating another edges between them
            if not dsu.isConnected(u, v):
                # create connection
                if dsu.union(u, v):
                    # weight update
                    mstWt += wt
                
        return mstWt