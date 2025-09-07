'''
LC 787: Cheapest Flights Within K Stops
There are n cities connected by some number of flights. 
You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. 
If there is no such route, return -1
'''
from collections import defaultdict
from collections import deque
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list) # Create adjacency list
        dist = [float('inf')] * n
        
        for s, d, c in flights:
            adj_list[s].append([d, c]) # Adjacency list contains the target node and the cost
        queue = deque()
        queue.append([0, src, 0]) # Stops, source, cost so far 
        while queue:
            stop, node, cost = queue.popleft()
            if stop > k:
                continue
            for adjnode, flight_cost in adj_list[node]:
                if c[adjnode] > cost + flight_cost and stop <= k:
                    dist[adjnode] = cost + flight_cost  # Update to the cheapest value
                    queue.append([stop+1, adjnode, cost+flight_cost]) # Add a stop and update the cost
        if dist[dst] == float('inf'):
            return -1
        return dist[dst]
# TC: O(N + EK) : O(N) to initialize dist array and O(EK) to iterate over the edges, atmost K times
# SC: O(N + EK) Space complexity: At most EK edges are processed on the queue. O(E) for adjacency list, O(N) for the dist array

    def findCheapestPriceDijstra(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        
        for s, d, c in flights:
            adj_list[s].append([d, c])
        costs = [float('inf')] * n
        pq = []
        heapq.heappush(pq, (0, src, 0))
        while pq:
            steps, node, cost = heapq.heappop(pq)
            if steps <= k and node in adj_list:
                for nextNode, flight_cost in adj_list[node]:
                    if flight_cost + cost < costs[nextNode]:
                        costs[nextNode] = flight_cost + cost
                        heapq.heappush(pq, (steps + 1, nextNode, flight_cost+cost))
        return costs[dst] if costs[dst] != float('inf') else -1
# O(N + EKlog(EK))): O(N) for the costs array initialization, O(EKlog(EK)) to push an element on the stack (O(EK) to pop)
# O(N + EK): O(N) For the costs array, O(EK) for the heapq as it will have max of K