'''
Queue Removals
You're given a list of n integers arr, which represent elements in a queue (in order from front to back). 
You're also given an integer x, and must perform x iterations of the following 3-step process:
Pop x elements from the front of queue (or, if it contains fewer than x elements, pop all of them)
Of the elements that were popped, find the one with the largest value (if there are multiple such elements, 
take the one which had been popped the earliest), and remove it. For each one of the remaining elements that were popped 
(in the order they had been popped), decrement its value by 1 if it's positive (otherwise, if its value is 0, then it's left unchanged), 
and then add it back to the queue. Compute a list of x integers output, the ith of which is the 1-based index in the original array of the 
element which had been removed in step 2 during the ith iteration.
Example: n = 6 arr = [1, 2, 2, 3, 4, 5] x = 5 output = [5, 6, 4, 1, 2]
Values in Queue after each Iteration:  [5, 0, 1, 1, 2],  [0, 0, 0, 1], [0, 0, 0], [0, 0], []
'''


from collections import deque
from collections import defaultdict
# Add any extra import statements you may need here


# Add any helper functions you may need here


def findPositions(arr, x):
  
  def performIteration(x):
    max_val = -1
    max_index = -1
    temp_arr = []
    for _ in range(x):
      if not queue:
        break
      val = queue.popleft()
      if val[0] > max_val:
        max_val = val[0]
        max_index = val[1]
      temp_arr.append(val)
    for i in range(len(temp_arr)):
      if temp_arr[i] != (max_val, max_index):
        temp_val = temp_arr[i][0] - 1 if temp_arr[i][0] else 0
        queue.append((temp_val, temp_arr[i][1]))
    return max_index + 1
        
     
  id_map = defaultdict(int)
  cur_iter = 0
  queue = deque()
  return_arr = []
  for i, a in enumerate(arr):
    queue.append((a, i))
  for _ in range(x):
    return_arr.append(performIteration(x))
  return return_arr


print(findPositions([1, 2, 2, 3, 4, 5], 5))


'''
TC: O(n + x**x)
SC: O(n)
'''