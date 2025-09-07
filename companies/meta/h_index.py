'''
LC 274: H-Index
Given an array of integers citations where citations[i] is the number of citations a researcher 
received for their ith paper, return the researcher's h-index.
The h-index of a researcher is the largest integer h such that there are 
h papers with at least h citations.
'''
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        # Use counting sort here
        count_array = [0] * (len(citations) + 1)
        num_citations = len(citations)
        h_count = 0
        for c in range(len(citations)):
            if citations[c] > num_citations:
                count_array[num_citations] += 1
            else:
                count_array[citations[c]] += 1
        for c in range(len(count_array) - 1, -1, -1):
            h_count +=  count_array[c]
            if h_count >= c:
                return c
        return 0
    
hi = Solution().hIndex
print (hi([3,0,6,1,5])) # 3
print (hi([1,3,1])) # 1
print (hi([4, 0, 1, 3, 2])) 

    
# Time Complexity: O(N) where N is the number of elements in the citations array
# Space Complexity: O(N) as we are using an array of size N
# Alternately we could have sorted the array and then checked it but 
# that would have been O(NlogN) time complexity