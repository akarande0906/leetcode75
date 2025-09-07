'''
LC 169: Majority Element
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Example: Input = [3,2,3] Output = 3
Input = [2,2,1,1,1,2,2] Output: 2
'''
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq_map = defaultdict(int)
        n = len(nums)
        for num in nums:
            freq_map[num] += 1
            if freq_map[num] > n // 2:
                return num
        return -1
    
majelem = Solution().majorityElement
print (majelem([3,2,3]))
print (majelem([2,2,1,1,1,2,2]))
