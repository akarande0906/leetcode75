'''
LC 621: Task Scheduler
'''
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26 
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        freq.sort()
        # We subtract 1 as we want to find the max idle slots needed between the most frequent tasks
        max_freq = freq[25] - 1 
        idle_slots = max_freq * n 

        for i in range(24, -1, -1):
            if not freq[i]: # We dont need to consider this
                break
            # We subtract idle slots by the freq: We are using up the idle slots
            idle_slots -= min(max_freq, freq[i])
        
        # Add pending idle slots to the total number of tasks
        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)

# Time Complexity: O(m + n log n) where m is the number of tasks and n is the number of unique tasks. Since n is at max 26, we can consider it as O(m).
# Space Complexity: O(1) since we are using a fixed size array of size 26 for the frequency count.
sol = Solution()
print(sol.leastInterval(["A","A","A","B","B","B"], 2)) # 8
print(sol.leastInterval(["A","A","A","B","B","B"], 0)) # 6
print(sol.leastInterval(["A","A","A","B","B","B"], 1)) # 6
print(sol.leastInterval(["A","B","C","D","E","F","G"], 2)) # 7