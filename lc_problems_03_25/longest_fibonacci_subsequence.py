'''
LC 873: Longest Fibonacci Subsequence
'''

class Solution:
    # Greedy Solution
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        # Construct a set from the array
        num_set = set(arr)
        max_len = 0
        for i in range(len(arr) - 1):
            for j in range (i+1,len(arr)):
                length = 2
                prev, cur = arr[i], arr[j]
                while (prev+cur in num_set):
                    prev, cur = cur, prev + cur
                    length += 1
                    max_len = max(max_len, length)
        return max_len
    
    # TC : O(N^2)
    # SC : O(N)
    
    def lenLongestFibSubseq_v2(self, arr: list[int]) -> int:
        # Dynamic Programming
        num_set = set(arr)
        max_len = 0
        dp = {}
        for i in reversed(range(len(arr) - 1)):
            for j in reversed(range(i+1, len(arr))):
                prev, cur = arr[i], arr[j]
                if (prev + cur in num_set):
                    dp[(i,j)] = dp.get((j, arr.index(prev + cur)), 2) + 1
                    max_len = max(max_len, dp[(i,j)])
        return max_len if max_len >= 3 else 0

    # TC : O(N^2)
    # SC : O(N^2) # For the DP dict

longestFib = Solution().lenLongestFibSubseq_v2
print(longestFib([1,2,3,4,5,6,7,8]))
print(longestFib([1,3,7,11,12,14,18]))
