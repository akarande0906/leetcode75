'''
LC 1944: Number of Visible people in the Queue
'''
from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            count = 0
            h = heights[i]
            # While the stack has a shorter person, pop and add to count
            while stack and stack[-1] < h:
                stack.pop()
                count += 1
            # You add one more to the count because this indicates there 
            # is still someone taller or the same height as the current person
            if stack:
                count += 1
            res[i] = count
            stack.append(h)
        return res

sol = Solution()
print(sol.canSeePersonsCount([10,6,8,5,11,9]))
print(sol.canSeePersonsCount([5,1,2,3,10]))
print(sol.canSeePersonsCount([10,8,12,6,14,16]))
print(sol.canSeePersonsCount([10,8,12,6,14,7]))
print(sol.canSeePersonsCount([10,6,8,5,11,9,13]))