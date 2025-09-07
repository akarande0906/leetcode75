'''
Element Swapping
Given a sequence of n integers arr, determine the lexicographically smallest sequence which may be obtained from it 
after performing at most k element swaps,  each involving a pair of consecutive elements in the sequence.
Note: A list x is lexicographically smaller than a different equal-length list y if and only if, 
for the earliest index at which the two lists differ, x's element at that index is smaller than y's element at that index.
'''

def findMinArray(arr, k):
  i = 0
  while k > 0 and i < len(arr):
      # current chunk from current pointer to the number of k available at this point
      view = arr[i : i + k + 1]
      # index of the smallest value in the current view
      min_index = arr.index(min(view), i)
      # if smallest value is not the current value
      if min_index > i:
          # remove smallest item from the list
          min_val = arr.pop(min_index)
          # and insert it to the begging of the view
          arr.insert(i, min_val)
          # update remaining number of swaps
          k -= min_index - i
      i += 1
  return arr


print(findMinArray([5, 3, 1], 2))
print(findMinArray([8, 9, 11, 2, 1], 3))
print(findMinArray([8, 9, 11, 2, 1], 6))
print(findMinArray([1, 2, 3, 4, 5], 4))
      