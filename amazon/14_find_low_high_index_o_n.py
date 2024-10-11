'''
Given a sorted array of integers, return the low and high index of the given key. You must return -1 if the indexes are not found. The array length can be in the millions with many duplicates.
'''
def find_low_high_index(arr, key):
    low_id = -1
    high_id = -1
    n = len(arr)
    for i in range(n):
      if arr[i] > key:
        if low_id != -1:
          high_id = i - 1
        break
      elif arr[i] == key:
        if low_id == -1:
          low_id = i
        elif i == n - 1:
          high_id = i
    return [low_id, high_id]


if __name__ == '__main__':
   arr = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
   print(find_low_high_index(arr,4))
   print(find_low_high_index(arr,5))
   print(find_low_high_index(arr,6))
   arr = [1,2,2,2,46,8,8]
   print(find_low_high_index(arr,2))
