'''
Implement quick sort of an array with first element as pivot
'''
def partition(arr, low, high):
    pivot = arr[0]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            

def quickSort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[0]
    for i in range(1, len(arr)):
        left = []
        right = []
