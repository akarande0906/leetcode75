

import random

def _quick_select_(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)

    left = [elem for elem in arr if elem < pivot]
    right  = [elem for elem in arr if elem > pivot]
    mid  = [elem for elem in arr if elem == pivot]

    if len(left) > k:
        return _quick_select_(left, k)
    elif len(left) + len(mid) > k:
        return mid[0]
    else: 
        return _quick_select_(right, k - len(mid) - len(left))
        

def quick_select_median(arr):
    if len(arr) % 2 == 1: # Odd elements
        return _quick_select_(arr, len(arr)//2)

    else:
        return 0.5 * (_quick_select_(arr, len(arr)/2) + _quick_select_(arr, len(arr)/2 - 1))


print (quick_select_median( [12, 3, 5, 7, 4, 19, 26, 11 ] ))
print (quick_select_median( [12, 3, 5, 7, 4, 19, 26 ] ))


