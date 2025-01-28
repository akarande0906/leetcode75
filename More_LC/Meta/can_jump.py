'''
LC 55: Jump Game
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
'''
# We use greedy algirithm to solve this problem. 
# We start from the last index and keep track of the last index that can reach the current index.
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0
        
# Time Complexity: O(N) where N is the number of elements in the array
# Space Complexity: O(1) since we are not using any extra space

finder = Solution().canJump
print (finder([2,3,1,1,4])) # True
print (finder([3,2,1,0,4])) # False
print (finder([3,2,1,0,4])) # True