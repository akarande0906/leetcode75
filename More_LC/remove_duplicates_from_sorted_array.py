'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Eg. Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_ptr = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[cur_ptr]:
                cur_ptr += 1
                nums[cur_ptr] = nums[i]
            print (str(i) + ':' + str(cur_ptr))
        print (nums)
        return cur_ptr + 1

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(Solution().removeDuplicates([1,1,2]))

