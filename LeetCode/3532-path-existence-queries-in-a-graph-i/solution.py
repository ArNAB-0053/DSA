# DSU APPROACH 
# But for this problem it is a overkill 

# but it is a general answer for this kinda questions

# class DSU:
#     def __init__(self, n: int):
#         self.parents = list(range(n))
#         self.size = [1]*n

#     # Find the representative (root) of each component
#     def find(self, x: int):
#         if self.parents[x] == x:
#             return x
#         self.parents[x] = self.find(self.parents[x]) # path compression
#         return self.parents[x]

#     def union(self, a:int, b:int):
#         # finding the root parent
#         pa = self.find(a)
#         pb = self.find(b)

#         if pa == pb:
#             return 

#         # always smaller one merges to larger one
#         # from here we are ensuring pa always be bigger
#         if self.size[pa] < self.size[pb]:
#             # swapping
#             pa, pb = pb, pa

#         # merge pb to pa
#         self.parents[pb] = pa
#         # increase the size as well
#         self.size[pa] += self.size[pb]

#     def isConnected(self, u:int, v:int):
#         return self.find(u) == self.find(v)

# class Solution:
#     def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
#         dsu = DSU(n)

#         # connect adjacent indices if their values differ by at most maxDiff
#         for i in range(n-1):
#             if nums[i+1] - nums[i] <= maxDiff:
#                 dsu.union(i, i+1)

#         ans = []
#         for u, v in queries:
#             # finding if u and v have same root parent or not 
#             ans.append(dsu.isConnected(u, v))
        
#         return ans


# Shorter and code optimised way for this problem
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # creates component ID of node i
        pre = [0] * n

        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                # if different component generate new ID by adding +1
                pre[i] = pre[i-1] + 1
            else:
                # if same component then uses same previous ID
                pre[i] = pre[i-1]
        
        ans = []
        for u, v in queries:
            # checks wheather u and v have same ID or not in pre
            ans.append(pre[u] == pre[v])
        
        return ans