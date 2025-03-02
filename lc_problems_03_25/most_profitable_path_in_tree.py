'''
LC 2467: Most profitable path in a tree
'''
from collections import defaultdict, deque

class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        # We know that Bob can only move in one direction
        # So we first compute his path_time to the root node
        # Then we can check different paths for Alice and see the max path_time to a leaf node
        adj_list = defaultdict(list)
        path_time = {}

        def create_adj_list(parent, child):
            adj_list[parent].append(child)
            adj_list[child].append(parent)
        
        def bob_dfs(node, prev, time):
            if node == 0:
                path_time[node] = time
                return True
            neighbors = adj_list[node]
            for n in neighbors:
                if n == prev:
                    continue
                if bob_dfs(n, node, time + 1):
                    path_time[node] = time
                    return True
            return False

        for e in edges:
            create_adj_list(e[0], e[1])
        bob_dfs(bob, -1, 0)

        max_profit = float('-inf')
        queue = deque([(0, 0, -1, 0)])
        while queue:
            node, curr_profit, prev, time = queue.popleft()
            cur_amount = amount[node]
            if node in path_time:
                b_time = path_time[node]
                if b_time == time:
                    cur_amount = amount[node] // 2
                elif b_time < time:
                    cur_amount = 0
            neighbors = adj_list[node]
            if len(neighbors) == 1 and node != 0:
                # We've reached a leaf node
                max_profit = max(max_profit, curr_profit + cur_amount)

            for n in neighbors:
                if n != prev:
                    queue.append((n, curr_profit + cur_amount, node, time + 1))
        return max_profit
mostProfitablePath = Solution().mostProfitablePath
print(mostProfitablePath([[0,2],[1,4],[1,6],[2,4],[3,6],[3,7],[5,7]], 4, [-6896,-1216,-1208,-1108,1606,-7704,-9212,-8258]))
print(mostProfitablePath([[0,1]], 1, [-7280, 2350]))
print(mostProfitablePath([[0,1],[1,2],[1,3],[3,4]], 3, [-2,4,2,-4,6]))

# TC : O(n)
# SC : O(n)
                    
            
