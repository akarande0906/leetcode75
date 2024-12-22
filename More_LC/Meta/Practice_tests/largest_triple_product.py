'''
Largest Triple Products:
You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, 
for each index i (between 0 and n-1, inclusive), output[i] is equal to the product of the three largest elements 
out of arr[0..i] (or equal to -1 if i < 2, as arr[0..i] then includes fewer than three elements).
Note that the three largest elements used to form any product may have the same values as one another, 
but they must be at different indices in arr.
'''

import heapq

# Add any helper functions you may need here
def getMaxElems(arr, k):
    heap = []
    for a in range(k+1):
        if len(heap) == 3:
            if heap[0] < arr[a]:
                heapq.heappop(heap)
                heapq.heappush(heap, arr[a])
        else:
            heapq.heappush(heap, arr[a])
    prod = 1
    for _ in range(0,3):
        prod *= heapq.heappop(heap)
    return prod


def findMaxProduct(arr):
    ret_arr = []
    if len(arr) >= 1:
        ret_arr.append(-1)
    if len(arr) >= 2:
        ret_arr.append(-1)
        
    for a in range(2, len(arr)):
        ret_arr.append(getMaxElems(arr, a))      
    return ret_arr

print (findMaxProduct([1, 2, 3, 4, 5]))
print (findMaxProduct([2, 4, 7, 1, 5, 3]))