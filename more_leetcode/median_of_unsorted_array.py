'''
Median of an unsorted array using Quick Select
'''
import random

def quickselect_median(l, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) // 2, pivot_fn)
    else:
        return 0.5 * (quickselect(l, len(l) / 2 - 1, pivot_fn) +
                      quickselect(l, len(l) / 2, pivot_fn))


def quickselect(l, k, pivot_fn):
    """
    Select the kth element in l (0 based)
    :param l: List of numerics
    :param k: Index
    :param pivot_fn: Function to choose a pivot, defaults to random.choice
    :return: The kth element of l
    """
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        # Our element is in the low list of elements and we can inturn focus our search here
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # We got lucky and guessed the median. So we can just return any of the pivot elements,
        # which are equal
        return pivots[0]
    else:
        # Our median is in the high list, so we focus our search here
        # We need to subtract the number of elements in the low and mid lists
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)
    
print (quickselect_median( [12, 3, 5, 7, 4, 19, 26, 11 ] ))
print (quickselect_median( [12, 3, 5, 7, 4, 19, 26 ] ))

# Time complexity : Average O(n), Worst case: O(n^2)
# Space complexity: O(n) as our three arrays high, low, pivot have a total length of n