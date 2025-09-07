'''
LC 1046: Last Stone Weight
'''
import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # We can use a max heap here and smash the top two elements
        # by popping them. We get the difference in weights and check 
        # Push the diff back if it is non zero (Stones are not equal weights)
        # and repeat the process till we have one/zero stones left
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            # Pop the first two elements from the heap 
            # and smash them
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            sum_weight = abs(stone1 - stone2)
            if sum_weight:
                heapq.heappush(heap, -sum_weight)
        return -heap[0] if heap else 0

finder = Solution().lastStoneWeight
print(finder([2,7,4,1,8,1])) # 1
print(finder([2,2])) # 0
print(finder([1,3])) # 2
print(finder([1])) # 1
print(finder([])) 
print(finder([1,1,1,1,1,2])) 
print(finder([1,1,1,1,1,1,2])) 