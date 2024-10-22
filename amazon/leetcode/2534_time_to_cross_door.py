from collections import deque


# 0 = enter, 1 = exit

class Solution:
    def timeTakenToCrossDoor(self, arrival: list[int], state: list[int]):
        prevState = -1
        entry_q = deque()
        exit_q = deque()
        
        for inter in range(len(arrival)):
            if state[inter] == 0:
                entry_q.append((arrival[inter], inter))
            else:
                exit_q.append((arrival[inter], inter))
        result = [-1]*len(arrival)
        time = 0
        while entry_q or exit_q:
            enter_person, exit_person = None, None
            print (entry_q)
            print (exit_q)
            if len(entry_q) and entry_q[0][0] <= time:
                enter_person = entry_q[0]
            if len(exit_q) and exit_q[0][0] <= time:
                exit_person = exit_q[0]
            choice = None
            if enter_person and exit_person:
                if len(exit_q) and (prevState == 1 or prevState == -1):
                    choice = exit_q.popleft()
                    result[choice[1]] = time
                elif len(entry_q):
                    choice = entry_q.popleft()
                    result[choice[1]] = time
            elif enter_person and len(entry_q) and not exit_person:
                choice = entry_q.popleft()
                result[choice[1]] = time
            elif exit_person and len(exit_q) and not enter_person:
                choice = exit_q.popleft()
                result[choice[1]] = time
            if choice:
                prev_state = state[choice[1]]
            else:
                prev_state = -1
            time += 1
        return result


print (Solution().timeTakenToCrossDoor([0,1,1,2,4], [0,1,0,0,1]))
#print (Solution().timeTakenToCrossDoor([[0,0,0]], [1,0,1]))



