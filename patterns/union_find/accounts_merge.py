'''
LC 721: Accounts Merge
'''
from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.root = [x for x in range(size)]
        self.rank = [1] * size 
    
    def find(self, x):
        # Compress path 
        if x == self.root[x]:
            return x
        # Recursively update the root of every node in the path
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(self.root[x])
        rootY = self.find(self.root[y])
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootY] > self.rank[rootX]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        uf = UnionFind(len(accounts))
        emailToAccounts = {}

        # Map emails to accounts and merge accounts if it maps to multiple accounts
        for id, values in enumerate(accounts):
            for eid in range(1, len(values)):
                email = accounts[id][eid]
                if email not in emailToAccounts:
                    emailToAccounts[email] = id
                else: # Merge accounts
                    uf.union(id, emailToAccounts[email])
        
        # Regroup the emails by main account
        accountGroup  = defaultdict(list)
        for email, accountId in emailToAccounts.items():
            parentAcId = uf.find(accountId)
            accountGroup[parentAcId].append(email)
        
        # Return response in expected format
        result = []
        for accountId, emailList in accountGroup.items():
            acName = accounts[accountId][0]
            result.append([acName] + sorted(emailList))
        return result

accMerge = Solution().accountsMerge
print(accMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
print(accMerge([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]))
