'''
Implement insertion sort and print each iteration
'''
def insertionSort2(n, numlist):
    # Write your code here
    arr = list(map(int, numlist.split(' ')))
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] < arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
        print (' '.join(str(k) for k in arr))


insertionSort2(6, '1 4 3 5 6 2')           