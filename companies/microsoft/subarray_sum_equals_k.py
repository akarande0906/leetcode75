'''
Leetcode: 560: Subarray Sum equals k
'''
from typing import List

class Solution():
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        map = {}
        count = 0
        map[0] = 1 # Count of 0 sum is 1 : Base case

        for i, n in enumerate(nums):
            cur_sum += n
            if cur_sum - k in map:
                count += map[cur_sum - k] # Increment the count
            map[cur_sum] = map.get(cur_sum, 0) + 1
        return count

arr_sum = Solution().subarraySum
print(arr_sum([1,1,1], 2))
print(arr_sum([1,2,3], 3))
print(arr_sum([1,2,3,-4,6,-6], 2))
print(arr_sum([2,2,2,-2,-2], 2))
print(arr_sum([2,-1,2,-1,2,-1,2,-1], 1))
