'''
LC 295: Find median from Data Stream 
'''
import heapq

class MedianFinder:

    def __init__(self):
        # We will use two heaps here. 
        # such that the elements on the left are in ascending order 
        # and elements on the right are in descending order
        self.lo = [] # Min heap to store all the higher elements
        self.hi = [] # Max heap to store all the lower elements 

    def addNum(self, num: int) -> None:
        # If the hi heap has elements and the number is greater than the hi heap, store it there
        if self.hi and num >= self.hi[0]:
            heapq.heappush(self.hi, num)
        else: # In all other cases, store the elem in the lo heap. We negate the number fo simulate a max heap
            heapq.heappush(self.lo, -num)
        
        # Balance the heaps such that the diff between their sizes is at most one.
        if len(self.lo) - len(self.hi) > 1:
            heapq.heappush(self.hi, -heapq.heappop(self.lo))
        elif len(self.hi) - len(self.lo) > 1:
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
        
    def findMedian(self) -> float:
        # To find the median check if the number of elems are odd or even
        # If odd, then we can get max elem from the hi heap or the min element from the lo heap
        if (len(self.hi) + len(self.lo)) % 2: # Odd number of elems
            if len(self.hi) > len(self.lo):
                return self.hi[0] # Min elem from right side
            else:
                return -self.lo[0] # Max elem from the left side                                                               
        else: # Average of the min elem from the right and max elem from the left
            return (self.hi[0] - self.lo[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
assert obj.findMedian() ==  1.5
obj.addNum(3)
assert obj.findMedian() == 2.0