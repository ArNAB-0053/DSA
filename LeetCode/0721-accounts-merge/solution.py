class DSU:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.size = [1]*n

    def find(self, x: int):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a: int, b: int):
        pa, pb = self.find(a), self.find(b)

        if pa == pb:
            return
        
        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa

        self.parents[pb] = pa
        self.size[pa] += self.size[pb]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = DSU(n)

        # email -> first account index that owns this email
        # used to detect accounts that should be merged
        mapMailNode = {}

        for i, mails in enumerate(accounts):
            # ignore 0th index as it has name
            for mail in mails[1:]:
                # if the email doesn't exists in the map
                # then initilize with main account index
                if mail not in mapMailNode:
                    mapMailNode[mail] = i
                # but if exists 
                # means it needed be merged
                # so calling the union function to create connection
                else:
                    dsu.union(i, mapMailNode[mail])

        # creating merged mail from the map
        mergedMail = [[] for _ in range(n)]
        for node, acc_idx in mapMailNode.items():
            # to merged we need it to use it's root parent
            root_idx = dsu.find(acc_idx)
            mergedMail[root_idx].append(node)

        ans = [] # stores the real answer
        for i, mails in enumerate(mergedMail):
            if mails:
                # sorting the mails
                mails.sort()
                # accounts[i][0] = name
                # merging name and the sorted mails
                temp = [accounts[i][0]] + mails
                ans.append(temp)

        return ans

