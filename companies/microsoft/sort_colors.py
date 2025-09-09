'''
Leetcode 75: Sort Colors
'''
from typing import List
from collections import Counter

# Red = 0, White = 1, Blue = 2
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c = Counter(nums)
        cur_index = 0
        for color in range(0, 3):
            for count in range(c[color]):
                nums[cur_index] = color
                cur_index += 1
        print (nums)

Solution().sortColors([2,0,2,1,1,0])
Solution().sortColors([2,0,1])
Solution().sortColors([2,0,2,2,0])

# Time Complexity: O(n) since we iterate over the entire array to generate the Counter
# The second for loop also has TC of O(n) as we iterate over all elements once
            
