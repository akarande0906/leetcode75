'''
LC 283: Move Zeros
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example: Input: nums = [0,1,0,3,12] Output: [1,3,12,0,0]
'''

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the number of zeros
        count_zeros = 0
        lptr = 0
        for n in range(len(nums)):
            if not nums[n]:
                count_zeros += 1
            else:
                if lptr != -1:
                    nums[lptr] = nums[n]
                    lptr += 1
        for n in range(len(nums) - count_zeros, len(nums)):
            nums[n] = 0
        print (nums)

Solution().moveZeroes([0,1,0,3,12])
Solution().moveZeroes([0])
Solution().moveZeroes([0,1,3,12,0])
        

                    

                

        