'''
LC 582: Kill Process
'''
from collections import deque

class Solution:
    def killProcess(self, pid: list[int], ppid: list[int], kill: int) -> list[int]:
        children = {}
        def getChildren(parent, child):
            if not parent in children:
                children[parent] = []
            children[parent].append(child)
        
        for i in range(len(pid)):
            getChildren(ppid[i], pid[i])
        kill_array = []
        if not kill in children:
            return [kill]
        queue = deque()
        queue.append(kill)
        ret_arr = []
        while queue:
            cur_proc = queue.popleft()
            ret_arr.append(cur_proc)
            if cur_proc in children:
                child_procs = children[cur_proc]
                for c in child_procs:
                    queue.append(c)
        return ret_arr

# Time: O(n)
# Space: O(n)

kill_process = Solution().killProcess
print(kill_process([1,3,10,5], [3,0,5,3], 5))
print(kill_process([1,3,10,5], [3,0,5,3], 3))
print(kill_process([1,3,10,5], [3,0,5,3], 1))
print(kill_process([1], [0], 1))


