'''
Leetcode 621: Task Scheduler
'''
from typing import List
from collections import Counter, deque
from heapq import heappush, heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ctr = Counter(tasks)
        task_heap = []
        for val in ctr.values():
            # Push the counter values to max heap
            heappush(task_heap, -val)
        time = 0

        queue = deque()
        
        while task_heap or queue:
            time += 1
            if not task_heap:
                # No more tasks in queue, we can just take the final time from the queue
                time = queue[0][1]
            else:
                # Since it is a max heap, to subtract we add one
                cnt = heappop(task_heap) + 1 

                # Include the time at which this can run next
                # The times will be in increasing order
                if cnt: # This is to ensure that we only include tasks still pending a run
                    queue.append((cnt, time + n))
            
            if queue and queue[0][1] == time:
                # If the job is ready to be executed add it back to the heap
                heappush(task_heap, queue.popleft()[0])
        return time
    

leastInt = Solution().leastInterval
print(leastInt(["A","A","A","B","B","B"], 2))
print(leastInt(["A","C","A","B","D","B"], 1))
print(leastInt(["A","A","A", "B","B","B"], 3))


        
