'''
Leetcode 169: Majority Element
'''
from typing import List
from collections import Counter

class Solution: 
    def majorityElement(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        half = len(nums) // 2
        for key, val in cntr.items():
            if val > half: # Majority Element
                return key
        return -1
    
    # With O(1) space
    def majorityElement2(self, nums: List[int]) -> int:
        # First sort the list
        nums.sort()
        half = len(nums) // 2
        cur_max, cur_sum = 1, 1
        cur_elem = nums[0]
        for elem in nums[1:]:
            if cur_elem == elem:
                cur_sum += 1
                cur_max = max(cur_max, cur_sum)
                if cur_max > half:
                    return elem
            else:
                cur_elem = elem
                cur_sum = 1
        return elem

    
major = Solution().majorityElement
print(major([3,2,3]))
print(major([2,2,1,1,1,2,2]))

major = Solution().majorityElement2
print(major([3,2,3]))
print(major([2,2,1,1,1,2,2]))
print(major([1,2,2,3,3,3,3]))



