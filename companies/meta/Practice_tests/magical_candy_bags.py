'''
Magical Candy Bags
You have N bags of candy. The ith bag contains arr[i] pieces of candy, and each of the bags is magical!
It takes you 1 minute to eat all of the pieces of candy in a bag (irrespective of how many pieces of candy are inside), 
and as soon as you finish, the bag mysteriously refills. If there were x pieces of candy in the bag at the beginning of the minute, 
then after you've finished you'll find that floor(x/2) pieces are now inside.
You have k minutes to eat as much candy as possible. How many pieces of candy can you eat?
'''

import heapq

def maxCandies(arr, k):
    # Write your code here
    heap = []
    for i in range(len(arr)):
        heapq.heappush(heap, -(arr[i]))
        candy_sum = 0
    for _ in range(k):
        max_candy = abs(heapq.heappop(heap))
        candy_sum += max_candy
        heapq.heappush(heap, -(max_candy // 2))
    return candy_sum

print(maxCandies([2, 1, 7, 4, 2], 3))
print(maxCandies([19, 78, 76, 72, 48, 8, 24, 74, 29], 3))