'''
LC 547: Number of Provinces
'''
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
	# Some ranks may become obsolete so they are not updated
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        N = len(isConnected)
        uf = UnionFind(N)
        # First create the Union tree/array
        numberOfComponents = N
        for i in range(N):
            for j in range(i + 1, N):
                if isConnected[i][j] == 1 and uf.find(i) != uf.find(j):
                    numberOfComponents -= 1
                    uf.union(i, j)
        return numberOfComponents           
        
# TC: O(N^2) where N is the number of cities
# SC: O(N) where N is the number of cities

findProvinces = Solution().findCircleNum
# print(findProvinces([[1,1,1],[1,1,1],[1,1,1]]))
# print(findProvinces([[1,1,0],[1,1,0],[0,0,1]]))
print(findProvinces([[1,0,0],[0,1,0],[0,0,1]]))
