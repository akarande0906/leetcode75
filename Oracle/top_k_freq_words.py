'''
LC 692: Top K Frequent Words
'''
from collections import Counter
from typing import List
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_map = {}
        cnt = Counter(words)
        heap = []
        for word,freq in cnt.items():
            heapq.heappush(heap, (-freq, word))
        return [heapq.heappop(heap)[1] for _ in range(k)]
sol = Solution()
print(sol.topKFrequent(["i","love","leetcode","i","love","coding"], 2))
print(sol.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))
print(sol.topKFrequent(["i","love","leetcode","i","love","coding"], 3))
print(sol.topKFrequent(["aaa", "aa", "a"], 2))
      