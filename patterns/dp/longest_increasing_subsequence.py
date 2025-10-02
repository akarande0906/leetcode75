'''
Leetcode 300: Find the length of the longest increasing subsequence
'''
# Identify the pattern
# Break it into subproblems
# Find relationship between subproblems
# Generalize

from bisect import bisect_left
from typing import List

# Here we traverse the sqeuence and create a sequence such that:
# If the new number is greater than the last element of the sequence, append it as it adds to the sequence
# Else, insert it in sorted order. This ensures that the sequence is always increasing
# Finally return the length of the sequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub_seq = []
        for num in nums:
            # Binary search to find the index where this number is found
            i = bisect_left(sub_seq, num)
            # It means that the number is greataer than the elements in the array
            if i == len(sub_seq):
                sub_seq.append(num)
            else:
                # bisect returns the nearest element 
                sub_seq[i] = num
        return len(sub_seq)
    
    # Time complexity : O(N Log (N))
    # Space complexity: O(N)

    # Here we compute the max subseq length at any given point dynamically.
    # Finally we return the max value for all subsequences.
    def lengthOfLIS_DP(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n # As for each element by itself it can be seq of 1
        # See if we can keep adding to the sequence
        for i in range(1, n):
            # Starting at index j, what is the max subsequence length at index i?
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
    # Time complexity: O(N^2)
    # Space complexity: O(N)

lengthOfLIS = Solution().lengthOfLIS_DP
print(lengthOfLIS([3,1,8,2,5]))
print(lengthOfLIS([4,3,2,1,0]))
print(lengthOfLIS([1,5,4,6,2]))
print(lengthOfLIS([3,2,8,1,5]))
print(lengthOfLIS([1,2,3,4,5]))
print(lengthOfLIS([2,8,6,3,6,9,5]))
print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))


        