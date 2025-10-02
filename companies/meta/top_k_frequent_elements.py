'''
LC 347: Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example: Input: nums = [1,1,1,2,2,3], k = 2 Output: [1,2]
Input: nums = [1], k = 1 Output: [1]
'''
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_map = {}
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        freq_heap = []
        for num, freq in freq_map.items():
            if len(freq_heap) == k:
                if freq_heap[0][0] < freq:
                    heapq.heappop(freq_heap)
                    heapq.heappush(freq_heap, (freq, num))
            else:
                heapq.heappush(freq_heap, (freq, num))
        return [i[1] for i in freq_heap]

print (Solution().topKFrequent([1,1,1,2,2,3], 2))
print (Solution().topKFrequent([1], 1))

'''
Time Complexity: O(n) for the iteration over nums, We add k elements to the heap and then we push and pop to get O(nlogk) => O(nlogk)
Space Complexity: O(N) for the hashmap and O(K) for the heap => O(n+k)
'''