def pivot(arr):
    prefixarr = []
    prefsum = 0
    for i in range(len(arr)):
        prefsum += arr[i]
        prefixarr.append(prefsum)
    if prefsum == 0:
        return 0
    prefsum = 0
    print (prefixarr)
    for j in range(len(arr) -1, -1, -1):
        prefsum += arr[j]
        if prefsum == prefixarr[j]:
            return j
    return -1

def pivot2(arr):
    prefixarr = []
    prefsum = 0
    for i in range(len(arr)):
        prefsum += arr[i]
        prefixarr.append(prefsum)
    if prefsum == 0:
        return 0
    prevsum = 0
    for i in range(len(arr)):
        if  prevsum == prefsum - prefixarr[i]:
            return i
        prevsum += arr[i]
    return -1


print(pivot2([1, 2, 3, 4, 3, 2, 1]))
print(pivot2([1, 100, 50, -51, 1, 1]))
print(pivot2([1, 100, -50, -51, 1, -1]))
        
