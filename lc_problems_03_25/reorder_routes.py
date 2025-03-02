'''
LC 1466: Reorder Routes to Make All Paths Lead to the City Zero
'''
from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # Create adj list
        adj_list = defaultdict(list)
        redirect_count = 0
        for e in connections:
            # Since its directional we mark the directions as part of the adj list
            adj_list[e[0]].append((e[1], True))
            adj_list[e[1]].append((e[0], False))
        # Lets create a visited list and mark it once visited, starting with 0
        visited = set()

        def dfs(node, prev_node):
            nonlocal redirect_count
            visited.add(node)
            # Get each node from the queue and traverse its neighbors
            neighbors = adj_list[node]
            for n in neighbors:
                if n[0] != prev_node and n[0] not in visited:
                    dfs(n[0], prev_node)
                    if n[1]:
                        redirect_count += 1

        for i in range(n):
            if not i in visited:
                dfs(i, -1)
        return redirect_count
    
    # TC : O(n)
    # SC : O(n)

minReorder = Solution().minReorder
print(minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))
print(minReorder(5, [[1,0],[1,2],[3,2],[3,4]]))
print(minReorder(3, [[1,0],[2,0]]))
print(minReorder(3, [[1,0],[2,1]]))

