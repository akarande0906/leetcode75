'''
Balanced Split
Given an array of integers (which may include repeated integers), determine if there's a way to split the array 
into two subsequences A and B such that the sum of the integers in both arrays is the same, 
and all of the integers in A are strictly smaller than all of the integers in B.
Note: Strictly smaller denotes that every integer in A must be less than, and not equal to, every integer in B.
Return true if such a split is possible, and false otherwise.
Example 1: arr = [1, 5, 7, 1] output = true
We can split the array into A = [1, 1, 5] and B = [7].
Example 2 arr = [12, 7, 6, 7, 6] output = false
We can split the array into A = [6, 6, 7] and B = [7, 12] but 7 is present in A which is invalid
'''
def balancedSplitExists(arr):
  # First sort the array
  arr.sort()
  total = sum(arr)
  # if the total cannot be divided in half, we return false
  if total % 2:
    return False
  total = total / 2
  # Build the right array till we get half the sum
  for i in range (len(arr) -1, -1 , -1):
    total = total - arr[i]
    if total == 0:
      if arr[i] == arr[i-1]:
        return False
      else: 
        return True
    elif total < 0: 
      return False
    
print (balancedSplitExists([2, 1, 2, 5]))
print (balancedSplitExists([3, 6, 3, 4, 4]))
print (balancedSplitExists([12, 7, 6, 7, 6]))
print (balancedSplitExists([12, 15, 9, 9, 9]))
print (balancedSplitExists([1, 5, 7, 2, 5, 6]))