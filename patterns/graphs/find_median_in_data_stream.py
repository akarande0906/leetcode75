'''
Leetcode 295: Find Median from Data Stream
'''
import heapq

class MedianFinder:
    def __init__(self):
        # We use two heaps: A max heap on the left half and a min heap on the right half
        # That way we can keep the highest element on the left half and lowest element 
        # of the right half next to each other to find the median
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        # When adding a num check if it fits in the left or right queue
        if self.high and num >= self.high[0]:
            heapq.heappush(self.high, num)
        else:
            # This is a max heap
            heapq.heappush(self.low, -num)

        # Now lets balance the heaps so at max diff between the two elements is 1
        if len(self.low) - len(self.high) > 1: 
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) - len(self.low) > 1: 
            heapq.heappush(self.low, -heapq.heappop(self.high))  
    
    def findMedian(self) -> float:
        if (len(self.low) + len(self.high)) % 2: # Odd number of elems 
            # Now we can return the max or min elem from the heap which is longer
            if len(self.high) > len(self.low):
                return self.high[0]
            else:
                return -self.low[0]
        else: # For even number of elements take the mean between the two
            return (self.high[0] - self.low[0]) / 2
        
obj = MedianFinder()
obj.addNum(1)  # arr = [1]
obj.addNum(2)  # arr = [1, 2]
print(obj.findMedian()) # return 1.5 (i.e., (1 + 2) / 2)
obj.addNum(3)  # arr[1, 2, 3]
print(obj.findMedian()) # return 2.0


# TIme complexity: O(log(n)) # Pushing an element onto the heap
# Space complexity: O(n) to maintain the heaps


