import bisect

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        subseq = []
        for n in nums:
            index = bisect.bisect_left(subseq, n) # Binary search to find where the element would go in a sorted array
            print (str(index) + ': ' + str(n))
            if index >= len(subseq):
                subseq.append(n)
            else:
                subseq[index] = n
        return len(subseq)

print(Solution().lengthOfLIS([1,2,3,0,1,2,3]))
            
