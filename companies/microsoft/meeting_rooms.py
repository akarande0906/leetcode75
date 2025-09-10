'''
Leetcode 252: Meeting Rooms
'''
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        if len(intervals) <= 1:
            return True
        
        min_int, max_int = intervals[0]
        for interval in intervals[1:]:
            if interval[0] < max_int:
                return False
            else:
                min_int, max_int = interval[0], interval[1]

        return True

meet = Solution().canAttendMeetings
print(meet([[0,30],[5,10],[15,20]]))
print(meet([[7,10],[2,4]]))

# Time complexity: O(n . log n)
# Space complexity: O(1)