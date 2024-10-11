'''
56. Merge Intervals
'''

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        ret_arr = []
        intervals = sorted(intervals, key=lambda x: x [0])
        if len(intervals) == 1:
            return intervals
        min_val = intervals[0][0]
        max_val = intervals[0][1]
        for i in range(1, len(intervals)):
            l, r = intervals[i]
            if l <= max_val:
                max_val = max(max_val, r)
                min_val = min(min_val, r)
            else:
                ret_arr.append([min_val, max_val])
                min_val = l
                max_val = r
        ret_arr.append([min_val, max_val])
        return ret_arr
            
m = Solution().merge
print(m([[1,4],[4,5]]))
print(m([[1,3],[2,6],[8,10],[15,18]]))
print(m([[1,4],[0,4]]))
print(m([[1,4],[2,3]]))

