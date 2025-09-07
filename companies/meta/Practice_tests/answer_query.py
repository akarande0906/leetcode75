'''
Answer Queries:
Imagine a length-N array of booleans, initially all false. Over time, some values are set to true, 
and at various points in time you would like to find the location of the nearest true to the right of given indices.
You will receive Q queries, each of which has a type and a value. SET queries have type = 1 and GET queries have type = 2.
When you receive a SET query, the value of the query denotes an index in the array that is set to true. Note that these indices start at 1. 
When you receive a GET query, you must return the smallest index that contains a true value that is greater than or equal to the given index, 
or -1 if no such index exists.

Signature
int[] answerQueries(ArrayList<Query> queries, int N)
Input
A list of Q queries, formatted as [type, index] where type is either 1 or 2, and index is <= N
1 <= N <= 1,000,000,000
1 <= Q <= 500,000
Output
Return an array containing the results of all GET queries. The result of queries[i] is the smallest index that contains a true value that is greater than or equal to i, or -1 if no index satisfies those conditions.

Example: N = 5 queries = [[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]] output = [-1, 2, -1, 2]
The initial state of the array is [false, false, false, false, false].
The first query is GET 3, but no values in the array are true, so the answer is -1.
The second query is SET 2, so the value at index 2 is set to true.
The new state of the array is [false, true, false, false, false].
The third query is GET 1, and the index of the true value nearest to 1 (to the right) is 2.
The fourth query is GET 3, but no values to the right of index 3 are true.
The fifth query is GET 2, and the value at index 2 is true.
  '''

import heapq

class BoolArray:
    def __init__(self):
        self.query_resp = []
        self.min_index, self.max_index = float('inf'), float('-inf')
        self.heap = []
    
    def _setQuery_(self, query):
        type, index = query
        if type == 1:
            self.bool_array[index - 1] = True
            self.min_index = min(index-1, self.min_index)
            self.max_index = max(index-1, self.max_index)
        elif type == 2:
            if self.min_index != float('inf') and self.max_index != float('-inf') and \
            (index - 1) <= self.max_index:
                if self.min_index >= (index - 1):
                    self.query_resp.append(self.min_index + 1)
                    return
            else:
                for i in range(index - 1, len(self.bool_array)):
                    if self.bool_array[i]:
                        self.query_resp.append(i + 1)
                        return
        self.query_resp.append(-1)
        
    def answerQueries(self, queries, N):
        self.N = N
        self.bool_array = [False] * N

        for q in queries:
            #self._setQuery_(q)
            self._heapQuery_(q)
        return self.query_resp

    def _heapQuery_(self, query):
        type, index = query
        if type == 1 and len(self.heap) < self.N:
            heapq.heappush(self.heap, index - 1)
        elif type == 2:
            if not self.heap:
                self.query_resp.append(-1)
            else:
                backup_array = []
                while self.heap and self.heap[0] < (index - 1):
                    backup_array.append(heapq.heappop(self.heap))
                if self.heap:
                    self.query_resp.append(self.heap[0] + 1)
                else:
                    self.query_resp.append(-1)
                while backup_array:
                    heapq.heappush(self.heap, backup_array.pop())
       
  
print (BoolArray().answerQueries([[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]], 5))

  
