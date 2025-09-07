'''
LC 325: Maximum Size Subarray Sum Equals k
Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k.
If there isn't one, return 0 instead.
'''
class Solution:
    def maxSubArrayLen(self, nums: list[int], k: int) -> int:
        # Compute prefix sums
        prefix_sums = {}
        max_len = 0
        total_sum = 0 
        for i in range(len(nums)):
            total_sum += nums[i]
            if total_sum == k:
                max_len = i + 1
            if total_sum - k in prefix_sums:
                cur_len = i - prefix_sums[total_sum - k]
                max_len = max(max_len, cur_len)
            if total_sum not in prefix_sums:
                prefix_sums[total_sum] = i
        return max_len

print(Solution().maxSubArrayLen([1,-1,5,-2,3], 3))
print(Solution().maxSubArrayLen([-2,-1,2,1], 1))
print(Solution().maxSubArrayLen([1,2,3,4,5], 10))
print(Solution().maxSubArrayLen([1,2,3,4,5], 11))
print(Solution().maxSubArrayLen([1,-2,6,-1,6], 10))
print(Solution().maxSubArrayLen([-1,-2,6,7], 10))

# Time Complexity: O(n)
# Space Complexity: O(n)            



            