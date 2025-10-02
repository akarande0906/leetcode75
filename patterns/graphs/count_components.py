'''
Leetcode 323: Number of Connected Components in Undirected Graph
'''
from typing import List
from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for e in edges:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])
        visited = set()

        def dfs(node):
            visited.add(node)
            nbrs = adj_list[node]
            for nbr in nbrs:
                if not nbr in visited:
                    dfs(nbr)

        components = 0
        for id in range(n):
            if id not in visited:
                dfs(id)
                components += 1
        return components

ctr = Solution().countComponents
print (ctr(5, [[0,1],[1,2],[3,4]]))
print (ctr(5, [[0,1],[1,2],[2,3],[3,4]]))

        

            
            

        



