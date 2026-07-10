from collections import defaultdict, deque

class Solution:
    def findOrder(self, words):
        # Topo Sort (Kahn's algorithm)

        # following slight different approach here
        # instead of normal TopoSort here
        # taking adj as set for not include duplicats
        # and using indegree as dictionary to store as characters

        adj = defaultdict(set)
        indegree = defaultdict(int)

        # initials
        # indegree = {
        #     a: 0,
        #     b: 0,
        #     c: 0,
        #     d: 0
        #     ...
        # }
        for wrd in words:
            for ch in wrd:
                indegree[ch] = 0

        # building graph
        # intuition:
        # first differing character determines the order.
        # if w1[j] != w2[j], then w1[j] must come before w2[j]
        # in the alien language because the dictionary is already sorted.
        for i in range(len(words)-1):
            # to compare current and next word
            w1 = words[i]
            w2 = words[i+1]

            # edge cases, e.g. ["abcd", "abc"]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            min_len = min(len(w1), len(w2))

            for j in range(min_len):
                u, v = w1[j], w2[j]
                # if current indexed element for w1 and w2 not equal
                # means we need to compare and add to adjacency list
                if u != v:
                    # this 'if' is for indegree
                    # adj is a set so for it using this condition - no need
                    # but this check is needed so indegree is incremented only
                    # when a new edge is actually added
                    if v not in adj[u]:
                        # as given `words` is sorted for align language
                        # means `u` comes before `v` for them
                        adj[u].add(v) # u -> v
                        indegree[v] += 1
                    break # break if anything added

        q = deque()
        # stores all the node(here character) with indegree 0
        for key in indegree:
            if indegree[key] == 0:
                q.append(key)

        # main topo sort loop
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)

            for it in adj[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    q.append(it)
        
        # needs string to be returned
        
        # if cycle return ""
        if len(topo) != len(indegree):
            return ""
            
        return "".join(topo)
