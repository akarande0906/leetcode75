'''
LC 1004: Max Consecutive Ones III: 
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]  => Two zeroes at indices 5 and 10 are flipped
'''

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        lptr = rptr = 0
        max_sub_array = 0
        num_zeros = num_ones = 0
        while lptr <= rptr and rptr < len(nums):
            if not nums[rptr]:
                num_zeros += 1
            else:
                num_ones += 1
            if num_zeros <= k:
                max_sub_array = max(max_sub_array, num_ones + num_zeros)
            else:
                while nums[lptr]:
                    lptr += 1
                    num_ones -= 1
                while lptr < len(nums) and not nums[lptr] and num_zeros > k:
                    lptr += 1
                    num_zeros -= 1
            rptr += 1
        return max_sub_array
    
print (Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print (Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
print (Solution().longestOnes([0,0,1,1,1,0,0], 0))