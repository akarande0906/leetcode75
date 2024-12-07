'''
LC 977: Squares of Sorted Array
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Example 1: Input: nums = [-4,-1,0,3,10] Output: [0,1,9,16,100]
Example 2: Input: nums = [-7,-3,2,3,11] Output: [4,9,9,49,121]
Can you solve this in O(n) time
'''
from collections import deque

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        sq_arr = []
        # Stack can be used here, deque is an overhead
        queue = deque()
        for i in range (len(nums)):
            if nums[i] < 0:
                queue.append(nums[i] ** 2)
            elif nums[i] == 0:
                sq_arr.append(0)
            else:
                square = nums[i] ** 2
                while queue and square > queue[-1]:
                    sq_arr.append(queue.pop())
                sq_arr.append(square)
        while queue: # Any residual elements if all elements were negative
            sq_arr.append(queue.pop())

        return sq_arr
'''
Time Complexity: O(n)     SC: O(n) for the queue
'''

'''
Alternate solution: 2 pointer : O(1) space complexity
def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sq_arr = [0] * n
        left = 0
        right = n - 1
        for i in range (n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            sq_arr[i] = square * square
        return sq_arr
'''

squarer = Solution().sortedSquares
print (squarer([-4,-1,0,3,10]))
print (squarer([-7,-3,2,3,11]))
print (squarer([-10,-9,-8,-7,-6,-5,-3,-1,0]))
