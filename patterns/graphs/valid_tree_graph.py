'''
Leetcode 261: Graph Valid Tree
'''
from typing import List
from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # THere are two properties of a graph that make it a tree:
        # All nodes are connected and there is no loop connecting back to a visited node.

        adj_list = defaultdict(list)
        for e in edges:
            # Since its a undirected graph
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])
        
        visited = set()

        queue = deque([(0, -1)]) # Where 0 is the starting node and -1 is the previous node where we came from
        
        while queue:
            node, prev = queue.popleft()
            if node in visited:
                # If we have already visited a node, then this means we have encountered a loop
                return False
            # Add the node to the visited set
            visited.add(node)
            # Get its neighbors
            for nbr in adj_list[node]:
                if nbr != prev: # We dont want to revisit the prev node since we came from there
                    queue.append((nbr, node)) # Add the neighbor and the node as its prev node
        
        return n == len(visited)
    
validTree = Solution().validTree
print(validTree(5, [[0,1],[0,2],[0,3],[1,4]]))
print(validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))

        