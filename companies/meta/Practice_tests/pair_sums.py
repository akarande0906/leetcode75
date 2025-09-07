'''
Pair Sums
Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
If an integer appears in the list multiple times, each copy is considered to be different; that is, 
two pairs are considered different if one pair includes at least one array index which the other doesn't,  even if they include the same values.
Example 1: n = 5 k = 6 arr = [1, 2, 3, 4, 3] output = 2
The valid pairs are 2+4 and 3+3.
Example 2: n = 5 k = 6 arr = [1, 5, 3, 3, 3] output = 4
There's one valid pair 1+5, and three different valid pairs 3+3 (the 3rd and 4th elements, 3rd and 5th elements, and 4th and 5th elements).
'''
from collections import defaultdict

def numberOfWays(arr, k):
   # Write your code here
    num_ways = 0
    map = defaultdict(int)
    for i in range(len(arr)):
      map[arr[i]] += 1
    for i in range(len(arr)):
      if k - arr[i] in map:
        if k == 2 * arr[i] and map[arr[i]] > 1:
          repeats = map[arr[i]]
          num_ways += (repeats * (repeats - 1))//2
        elif k != 2 * arr[i]:
          num_ways += map[k - arr[i]]
        map[arr[i]] = 0
    return num_ways

print (numberOfWays([1, 2, 3, 4, 3], 6))
print (numberOfWays([1, 5, 3, 3, 3], 6))
print (numberOfWays([1, 5, 3, 3, 3, 3], 6))