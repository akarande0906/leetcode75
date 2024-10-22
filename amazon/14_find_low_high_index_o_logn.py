'''
Given a sorted array of integers, return the low and high index of the given key. You must return -1 if the indexes are not found. The array length can be in the millions with many duplicates.
'''
def find_low_index(arr, key):
    low = 0
    high = len(arr) - 1
    mid = int(high / 2)

    while low <= high:
        mid_elem = arr[mid]

        if mid_elem < key:
            low = mid + 1
        else: # mid elem is >= key
            high = mid - 1

        mid = low + int((high - low) / 2)

    if low < len(arr) and arr[low] == key:
        return low

    return -1

def find_high_index(arr, key):
    low = 0
    high = len(arr) - 1
    mid = int(high / 2)

    while low <= high:
        mid_elem = arr[mid]

        if mid_elem <= key:
            low = mid + 1
        else:
            high = mid - 1

        mid = low + int((high - low) / 2);
    
    if high == -1:
        return high

    if high < len(arr) and arr[high] == key:
        return high

    return -1

def find_low_high_index(arr, key):
    low = find_low_index(arr, key)
    high = find_high_index(arr, key)
    
    return [low, high]

if __name__ == '__main__':
   arr = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
   print(find_low_high_index(arr,4))
   print(find_low_high_index(arr,5))
   print(find_low_high_index(arr,6))
   arr = [1,2,2,2,46,8,8]
   print(find_low_high_index(arr,2))
   arr = [1,1,1,2,46,8,8]
   print(find_low_high_index(arr,2))
