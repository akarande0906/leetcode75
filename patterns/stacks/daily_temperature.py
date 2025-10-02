'''
Leetcode 739: Daily Temparature
'''
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        # First initialize the result with all 0s
        answer = [0] * len(temperatures)
        for cur_day, cur_temp in enumerate(temperatures):
            # Pop the stack till we see a day that is lesser than 
            while stack and temperatures[stack[-1]] < cur_temp:
                prev_day = stack.pop()
                answer[prev_day] = cur_day - prev_day
            stack.append(cur_day)
        return answer




dailyTemp = Solution().dailyTemperatures
print(dailyTemp([73,74,75,71,69,72,76,73]))
'''
[1,1,4,2,1,1,0,0]
'''