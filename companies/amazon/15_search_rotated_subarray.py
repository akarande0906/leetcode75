'''
Search for a given number in a sorted array, with unique elements, that has been rotated by some arbitrary number. Return -1 if the number does not exist. Assume that the array does not contain duplicates.
'''
def binary_search_rotated(arr, key):
    return rotated_b_search(arr, 0, len(arr) - 1, key)   


def rotated_b_search(arr, low, high, key): 
    if low <= high:
       mid = low + int((high-low)/2)
       print ('LOW: ' + str(low))
       print ('MID: ' + str(mid))
       print ('HIGH: ' + str(high))
       if arr[mid] == key:
          return mid
       if arr[low] < arr[mid]: # Left subarray is sorted
          if arr[mid] > key and key >= arr[low]:
              return rotated_b_search(arr, low, mid - 1, key)
          else:
              return rotated_b_search(arr, mid + 1, high, key)
       else:
          if arr[mid] < key and key <= arr[high]:
              return rotated_b_search(arr, mid + 1, high, key)
          else:
             return rotated_b_search(arr, low, mid - 1, key)
    else:
       return -1


arr = [176, 188, 199, 200, 210, 222, 1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162]
key = 99
print(arr)
print(binary_search_rotated(arr, key))
