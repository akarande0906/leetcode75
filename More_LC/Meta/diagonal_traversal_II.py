'''
LC 1424: Diagonal Traverse II
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.
Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
'''
'''   Solution works but times out 
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        final_arr = []
        n = len(nums)
        max_cols = 0
        for i in range(n):
            r, c = i, 0
            max_cols = max(max_cols, len(nums[r]))
            while r >= 0:
                if c < len(nums[r]):
                    final_arr.append(nums[r][c])
                r, c = r-1, c+1
        for j in range(1, max_cols):
            r, c = n -1, j
            while r >= 0:
                if c < len(nums[r]):
                    final_arr.append(nums[r][c])
                r, c = r-1, c+1
        return final_arr
'''
from collections import deque
class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        queue = deque()
        queue.append((0,0))
        return_arr = []
        while queue:
            row, col = queue.popleft()
            return_arr.append(nums[row][col])
            # For col 0, add both the cell below and the cell to the right
            # For all other cells only the cell to the right. This will cover the next diagonal
            # Dont add the node if its out of bounds
            if col == 0 and row + 1 < len(nums):
                queue.append((row+1, col))
            if col + 1 < len(nums[row]):
                queue.append((row, col+1))
        return return_arr
    
finder = Solution().findDiagonalOrder
print (finder([[1,2,3],[4,5,6],[7,8,9]]))
print (finder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))
'''
Time Complexity: O(n) where n is the number of elements in the grid. Queue operations are O(1)
Space Complexity: O(sqrt(n)) which is max items populated in the diagonal
'''
