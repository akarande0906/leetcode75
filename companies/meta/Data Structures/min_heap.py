'''
Implement Min Heap data structure
'''
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1)// 2
    
    def leftChild(self, index):
        return 2*index + 1
    
    def rightChild(self, index):
        return 2*index + 2
    
    def hasLeftChildren(self, index):
        return self.leftChild(index) < len(self.heap)
    
    def hasRightChildren(self, index):
        return self.rightChild(index) < len(self.heap)
    
    def _heapify_up_(self, index):
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            # Swaps the elements if the child has a smaller element than the parent
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up_(len(self.heap) - 1)
    
    def _heapify_down(self, index):
        # We need to find the smallest element and recaliberate
        smallest = index
        if self.hasLeftChildren(index) and self.heap[self.leftChild(index)]  < self.heap[smallest]:
            smallest = self.leftChild(index)
        elif self.hasRightChildren(index) and self.heap[self.rightChild(index)]  < self.heap[smallest]:
            smallest = self.rightChild(index) 
        if smallest != index: 
            # Swap the elements 
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index] 
            self._heapify_down(smallest)
    
    def removeMinElement(self):
        if not self.heap:
            raise IndexError('Cannot Remove from empty heap')
        minVal = self.heap[0]
        cur_val = self.heap.pop()
        if self.heap:
            self.heap[0] = cur_val
            self._heapify_down(0)
        return minVal
                
    def getMinValue(self): 
        if not self.heap: 
            raise IndexError("get_min from an empty heap") 
        return self.heap[0] 
 
    def is_empty(self): 
        return len(self.heap) == 0 
 
    def size(self): 
        return len(self.heap) 
 
    def __str__(self): 
        return str(self.heap) 
    
    
if __name__ == "__main__": 
    min_heap = MinHeap() 
    
    # Insert elements 
    min_heap.insert(5) 
    min_heap.insert(3) 
    min_heap.insert(8) 
    min_heap.insert(1) 
    
    print("Heap:", min_heap)  # Output: Heap: [1, 3, 8, 5] 
    
    # Get the minimum element 
    print("Minimum:", min_heap.getMinValue())  # Output: Minimum: 1 
    
    # Remove the minimum element 
    min_heap.removeMinElement() 
    print("Heap after removing min:", min_heap)  # Output: Heap after removing min: [3, 5, 8] 