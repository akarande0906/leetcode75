'''
LC 547: Number of Provinces
'''
from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        N = len(isConnected)
        visited = [False] * N
        # First create adjacency list
        adj_list = defaultdict(list)
        for i in range(N):
            for j in range(i+1, N):
                if isConnected[i][j] == 1:
                    adj_list[i].append(j)
        
        def dfs(node):
            visited[node] = True
            for i in range(N):
                if isConnected[node][i] and not visited[i]:
                    dfs(i)
       
        provinces = 0
        for i in range(N):
            if not visited[i]:
                provinces += 1
                dfs(i)
        return provinces
    
# TC: O(N^2) where N is the number of cities
# SC: O(N) where N is the number of cities
findProvinces = Solution().findCircleNum
print(findProvinces([[1,1,1],[1,1,1],[1,1,1]]))
print(findProvinces([[1,1,0],[1,1,0],[0,0,1]]))
print(findProvinces([[1,0,0],[0,1,0],[0,0,1]]))
        
                


        