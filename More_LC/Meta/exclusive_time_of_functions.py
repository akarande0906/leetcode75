'''
LC 636: Exclusive Time of Functions
On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.
Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, 
and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. 
Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.
You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". 
For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. 
Note that a function can be called multiple times, possibly recursively.
A function's exclusive time is the sum of execution times for all function calls in the program. 
For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.
Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.
'''
class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        stack = []
        total_time = [0] * n
        prev_time = -1
        for log in logs:
            c_log, c_type, c_time = log.split(':')
            c_log, c_time = int(c_log), int(c_time)
            if c_type == 'start':
                # Check if there is an existing log on the stack
                # If so update the run time
                if stack:
                    total_time[stack[-1]] += c_time - prev_time 
                stack.append(c_log)
            else:
                total_time[stack.pop()] += c_time - prev_time + 1
            # Everytime we update previous time. For end time it has to be 
            # incremented by 1 as the next job can only start in the next cycle
            prev_time = c_time + int(c_type == 'end')
        return total_time

et = Solution().exclusiveTime
print(et(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))
print(et(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))
print(et(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))
print(et(2, ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]))
