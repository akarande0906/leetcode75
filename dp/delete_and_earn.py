'''
LC 740: Delete and Earn
'''
from typing import List
from collections import defaultdict

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_num = 0
        
        for num in nums:
            points[num] += num
            max_num = max(max_num, num)

        max_points = [0] * (max_num + 1)
        max_points[1] = points[1]

        for num in range(2, len(max_points)):
            max_points[num] = max(max_points[num - 1], max_points[num - 2] + points[num])
        return max_points[max_num]
    
    # WE can reduce this to O(1) space by using two variables instead of an array
    def deleteAndEarn_v2(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_num = 0
        
        for num in nums:
            points[num] += num
            max_num = max(max_num, num)

        first = 0
        second = points[1]

        for num in range(2, max_num + 1):
            first, second = second, max(second, first + points[num])
        return second

deleteEarn = Solution().deleteAndEarn
print(deleteEarn([3, 4, 2]))
print(deleteEarn([2, 2, 3, 3, 3, 4]))

# TC : O(N)
# SC : O(N)
