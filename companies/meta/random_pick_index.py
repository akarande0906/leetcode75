'''
LC 398: Random Pick Index
Given an integer array nums with possible duplicates, randomly output the index of a given target number. 
You can assume that the given target number must exist in the array.
Implement the Solution class:
Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target. 
If there are multiple valid i's, then each index should have an equal probability of returning.
'''
from collections import defaultdict
from random import choice
class Solution:

    def __init__(self, nums: list[int]):
        self.hash_map=defaultdict(list)
        for i,n in enumerate(nums):
            self.hash_map[n].append(i)

    def pick(self, target: int) -> int:
        if not target in self.hash_map:
            return -1
        elif len(self.hash_map[target]) == 1:
            return self.hash_map[target][0]
        else:
            return choice(self.hash_map[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)