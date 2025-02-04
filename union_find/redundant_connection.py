'''
LC 684: Redundant Connection 
'''
class UnionFind:
    def __init__(self, size):
        self.rank = [1] * size
        self.root = list(range(size))
    
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        # If the two roots match it means that we are creating a cycle
        if rootX == rootY:
            return False 
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
            self.rank[rootX] += self.rank[rootY]
        else:
            self.root[rootX] = rootY
            self.rank[rootY] += self.rank[rootX]
        return True

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        uf = UnionFind(len(edges))
        for edge in edges:
            # IF the two edges have a same root we have a cycle so we can return this 
            # as the redundant node
            if not uf.union(edge[0] - 1, edge[1] - 1):
                return edge
        return []

# TC : O(N)  [ The Union Find algorithm has a constant time complexity ]
# SC : O(N)  [ The Union Find algorithm has a constant space complexiity ]

redConn = Solution().findRedundantConnection
print(redConn([[1,2],[1,3],[2,3]]))
print(redConn([[1,2],[2,3],[3,4],[1,4],[1,5]]))
