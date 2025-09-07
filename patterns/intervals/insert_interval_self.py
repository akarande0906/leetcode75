class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        new_arr = []
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        n = len(intervals)
        i = 0
        while i < n and newInterval[0] > intervals[i][1]:
            new_arr.append(intervals[i])
            i += 1
        maxVal = newInterval[1]
        minVal = newInterval[0]
        while i < n and newInterval[1] >= intervals[i][0]:
            minVal = min(minVal, min(newInterval[0], intervals[i][0]))
            maxVal = max(maxVal, max(newInterval[1], intervals[i][1]))
            i += 1
        new_arr.append([minVal, maxVal])
        while i < n:
            new_arr.append(intervals[i])
            i += 1
        return new_arr            

sol = Solution()
print (sol.insert([[1,3],[6,9]], [2,5]))        
print (sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
