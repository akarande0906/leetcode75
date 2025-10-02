'''
Leetcode 239: Sliding Window Maximum
'''
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        max_array = []
        for n in range(len(nums)):
            # while the numer on the queue is less than the current number
            # We can remove those numbers from the queue since they are no longer max
            while queue and nums[queue[-1]] < nums[n]:
                queue.pop()
            # At the end of this the max will remain on the queue
            queue.append(n)
            if queue[0] == n - k: # We have reached the window length
                queue.popleft()
            # Once we reach the window size number of elements
            # Populate the max array
            if n >= k - 1:
                # The left most element will be the max in the window
                max_array.append(nums[queue[0]])
        return max_array

maxWin = Solution().maxSlidingWindow
print(maxWin([1,3,-1,-3,5,3,6,7],3))
print(maxWin([1],1))
print(maxWin([1,2,1,0,4,2,6],3))





