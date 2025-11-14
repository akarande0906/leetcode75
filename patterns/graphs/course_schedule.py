'''
Leetcode 207: Course Schedule
'''
from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses
        ans_array = []

        for pair in prerequisites:
            course = pair[0]
            prereq = pair[1]

            # We create an adj list of prereqs to followers
            adj_list[prereq].append(course)
            # Increase the in degree of a course that is how many prereqs a  course has
            in_degree[course] += 1

        queue = deque()
        for course in range(numCourses):
            # Look for all courses that can start immediately
            # without prerequisites
            if in_degree[course] == 0:
                queue.append(course)
        
        while queue:
            current_course = queue.popleft()
            # Any course we put on the queue can be executed without waiting
            ans_array.append(current_course)

            for next_course in adj_list[current_course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        return True if len(ans_array) == numCourses else False
    
canFinish = Solution().canFinish
print(canFinish(2, [[1,0],[0,1]]))
print(canFinish(2, [[1,0]]))

# Time Complexity: O(m+n) where m is the number of courses and n is the number of prereqs
# Space Complexity: O(m+n) as we store the number of courses and number of prereqs in the adj_list



