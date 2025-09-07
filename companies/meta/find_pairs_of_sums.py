'''
Given two unsorted arrays, find all pairs whose sum is k
For example:
arr1 = [1,2,4,5,7]
arr2 = [5,6,3,4,8]
k = 9
ans: [(1,8), (4,5), (5,4)]
'''

def findSumPairs(arr1, arr2, k):
    map = {}
    final_arr = []
    for a in arr1:
        map[k-a] = a
    for b in arr2:
        if b in map:
            final_arr.append((map[b], b))
    return final_arr

print(findSumPairs([1,2,4,5,7], [5,6,3,4,8], 9 ))