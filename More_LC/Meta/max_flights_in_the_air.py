'''
Given a list of flights represented by start and end times, 
find the max flights in the air at a given time.
The flight end time cannot overlap with another flight start time if they are the same value:
e.g. [2, 3] and [3, 4]
'''
from collections import deque

class Flight:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def maxFlightsInTheAir(arr):
    # First Sort the array by start times as this is when they will take off
    arr.sort(key=lambda x: x[0])
    '''
    flights_array = []
    for s, e in arr:
        flight = Flight(s, e)
    '''
    q = deque()
    q.append(arr[0])
    max_flights = 1
    for i in range(1, len(arr)):
        while q and q[0][1] < arr[i][0]:
            q.popleft()
        if q:
            flights = 1 + len(q)
            max_flights = max(max_flights, flights)
        q.append(arr[i])
    
    return max_flights

arr = [[4,8], [2,5], [17, 20], [10, 21], [9,18]]
print(maxFlightsInTheAir(arr))

arr = [[4,11], [2,5], [9, 20], [10, 21], [9,18]]
print(maxFlightsInTheAir(arr))

arr = [[4,11]]
print(maxFlightsInTheAir(arr))

        
        

    

