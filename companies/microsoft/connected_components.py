'''
Leetcode 323: Number of Connected Components in Undirected Graph
'''
from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_matrix = defaultdict(list)
        
        def create_adj_matrix():
            for e in edges:
                adj_matrix[e[0]].append(e[1])
                adj_matrix[e[1]].append(e[0])

        def dfs(node):  
            visited.add(node)
            # Get neighbors of node
            neighbors = adj_matrix[node]
            for ng in neighbors:
                if ng not in visited:
                    dfs(ng)

        components = 0
        visited = set()
        create_adj_matrix()

        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        return components

print(Solution().countComponents(5, [[0,1],[1,2],[3,4]]))       
print(Solution().countComponents(5, [[0,1],[1,2],[2,3],[3,4]]))



        
