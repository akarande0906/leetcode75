'''
Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.
All integers in array are in the range [0, 1,000,000,000].
Return true if B can be made equal to A, return false otherwise.
Example A = [1, 2, 3, 4] B = [1, 4, 3, 2] output = true  : After reversing the subarray of B from indices 1 to 3, array B will equal array A
'''
def are_they_equal(array_a, array_b):
  # Write your code here
  lptr = 0
  rptr = len(array_a) - 1
  while lptr <= rptr:
    if array_a[lptr] != array_b[lptr] and array_a[rptr] != array_b[rptr]:
      break
    if array_a[lptr] == array_b[lptr]:
      lptr += 1
    if array_a[rptr] == array_b[rptr]:
      rptr -= 1
  while lptr <= rptr:
    if array_a[lptr] != array_b[rptr]:
      return False
    lptr += 1
    rptr -= 1
  return True

print(are_they_equal([1, 2, 3, 4], [1, 4, 3, 2]))
print(are_they_equal([1, 2, 3, 4],[1, 2, 3, 5]))