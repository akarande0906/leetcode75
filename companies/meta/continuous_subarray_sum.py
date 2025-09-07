'''
LC 523: Continuous Subarray Sum
A good subarray is a subarray where:
Its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:
A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
Example: Input: nums = [23,2,4,6,7], k = 6 Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Input: nums = [23,2,6,4,7], k = 6 Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
'''
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix_sum = 0
        mod_seen = {0:-1} # Initialize the map
        for i in range(len(nums)):
            # At each index, check the remainder when sum is divided by k
            prefix_sum = (prefix_sum + nums[i]) % k
            # If we see a remainder repeated, check if the indices are different
            if prefix_sum in mod_seen:
                if i - mod_seen[prefix_sum] > 1:
                    return True
            else:
                mod_seen[prefix_sum] = i
        return False
            
checkSum = Solution().checkSubarraySum
print (checkSum([2,4], 6))
print (checkSum([23,2,6,4,7], 6))
print (checkSum([23,2,6,4,7], 13))


