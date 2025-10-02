'''
Leetcode 853: Car Fleet
'''
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        # Create a combined array 
        car_list = [[p, s] for p, s in zip(position, speed)]
        for p, s in sorted(car_list)[::-1]: # Start in reverse
            cur_time_at_dest = (target - p) / s
            # Check if the new car has a shorter time to get 
            # to the destination it will collide with the 
            # car thats on the stack
            if not stack or cur_time_at_dest > stack[-1]:
                # We dont put this car on the stack 
                # since once they converge the slower car 
                stack.append(cur_time_at_dest)
        return len(stack)
    
fleet = Solution().carFleet
print(fleet(12, [10,8,0,5,3], [2,4,1,1,3]))
print(fleet(10, [3], [3]))
print(fleet(100, [0,2,4], [4,2,1]))
print(fleet(10, [0,4,2], [2,1,3]))
                