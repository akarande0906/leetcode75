'''
'''
import math
from typing import List
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  #First sort the array
  S.sort()
  S.append(N+1+K)
  cur_min = 1
  diners = 0
  for diner in S:
    d_min = diner - K
    d_max = diner + K
    if d_min - cur_min > 0:
      # We can accomodate diners there
      # We divide by K+1 instead of K to 
      diners += math.ceil((d_min - cur_min) / (K+1))
    cur_min = d_max + 1
  return diners

print (getMaxAdditionalDinersCount(10, 1, 2, [2,6]))
print (getMaxAdditionalDinersCount(15, 2, 3,  [11, 6, 14]))
print (getMaxAdditionalDinersCount(15, 1, 2,  [2, 6]))

'''
X D X O X D X O X O X O X O X 

'''