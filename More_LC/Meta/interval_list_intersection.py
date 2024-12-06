'''
LC 986: Interval List Intersections
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. 
Each list of intervals is pairwise disjoint and in sorted order. Return the intersection of these two interval lists.
A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. 
For example, the intersection of [1, 3] and [2, 4] is [2, 3].
'''
class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        f_len = len(firstList)
        s_len = len(secondList)
        f_ptr = 0
        s_ptr = 0
        intersection = []
        while f_ptr < f_len and s_ptr < s_len:
            f_start, f_end = firstList[f_ptr]
            s_start, s_end = secondList[s_ptr]
            # Check if there is overlap
            max_start = max(f_start, s_start)
            min_end = min(f_end, s_end)
            # If there is an intersection we will find 
            # a start/end time that is a closed interval
            if max_start <= min_end:
                intersection.append([max_start, min_end])
            # Remove the interval with smaller end time
            if firstList[f_ptr][1] < secondList[s_ptr][1]:
                f_ptr += 1
            else:
                s_ptr += 1
        return intersection
    
intersect = Solution().intervalIntersection
print (intersect([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
print(intersect([[1,3],[5,9]], []))