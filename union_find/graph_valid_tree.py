'''
LC 261: Given a graph with n nodes labeled 0..n-1 and an edge list (a,b), determine if the graph is a valid tree.
'''
from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # For a tree the number of edges should be n - 1
        if len(edges) != n - 1:
            return False
        adj_list = defaultdict(list)
        
        def create_adj_list():
            for A, B in edges:
                adj_list[A].append(B)
                adj_list[B].append(A)
                
        create_adj_list()
        if len(adj_list) == 0:
            return n == 1
        visited = set()
        queue = deque()
        queue.append(0)
        visited.add(0)
        while queue:
            node = queue.popleft()
            
            for nbr in adj_list[node]:
                if nbr in visited:
                    continue
                queue.append(nbr)
                visited.add(nbr)
        return len(visited) == n
        
            
valid = Solution().validTree
print(valid(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))
print(valid(3, [[1,0],[2,0]]))
print(valid(4, [[0,1],[0,2],[1,2]]))
print(valid(5, [[0,1],[0,2],[0,3],[1,4]]))
print(valid(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))
