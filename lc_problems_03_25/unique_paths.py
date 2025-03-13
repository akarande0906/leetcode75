'''
LC 65: Unique Paths
'''
class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]
        for col in range(1, m):
            for row in range(1, n):
                d[col][row] = d[col - 1][row] + d[col][row - 1]
        return d[m - 1][n - 1]
# TC : O(m*n)
# SC : O(m*n)
    def uniquePaths_v2(self, m: int, n: int) -> int:
        _path_sum = 0
        def traverse(node, visited):
            nonlocal _path_sum
            if node == (m-1, n-1):
                _path_sum += 1
            else:
                directions = [(0,1),(1,0)]
                for d in directions:
                    new_node = (node[0] + d[0], node[1] + d[1])
                    if new_node[0] >= 0 and new_node[0] <= m - 1 and \
                        new_node[1] >= 0 and new_node[1] <= n - 1 and \
                        new_node not in visited:
                        visited.add(new_node)
                        traverse(new_node, visited)
                        visited.remove(new_node)
        traverse((0,0), set())
        return _path_sum


uniquePaths = Solution().uniquePaths_v2
print(uniquePaths(3, 7))
print(uniquePaths(3, 2))
print(uniquePaths(7, 3))
print(uniquePaths(3, 3))