'''
Leetcode 42: Trapping Rain Water
'''
from typing import List

'''
We set the left and right pointers to the edges
We check if the value at left pointer is less than the value at right pointer:
    That means that we can consider the difference between the highest wall on the left
    and the height at the left pointer, which will give us the current vol of water at that level
    Then we incrase the left pointer to proceed to the next row
    We update the max height on left to the current height if its greater.
Else we check the volume of water on the right and follow the same process, except we move to the left
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right = 0, 0
        left_ptr, right_ptr = 0, len(height) - 1
        volume = 0
        while left_ptr < right_ptr:
            if height[left_ptr] < height[right_ptr]:
                max_left = max(max_left, height[left_ptr])
                volume += max_left - height[left_ptr]
                left_ptr += 1
            else:
                max_right = max(max_right, height[right_ptr])
                volume += max_right - height[right_ptr]
                right_ptr -= 1
        return volume

trap = Solution().trap
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))
