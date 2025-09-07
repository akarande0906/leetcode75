class Solution:
    def findMin(self, nums: list[int]) -> int:
        lptr = 0
        rptr = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while True:
            if nums[lptr] < nums[rptr]:
                return nums[lptr]
            elif nums[lptr] > nums[lptr + 1]:
                return nums[lptr+1]
            else:
                lptr += 1

sol = Solution()
print (sol.findMin([3,4,5,1,2]))
print (sol.findMin([4,5,6,7,0,1,2]))
print (sol.findMin([11,13,15,17]))
print (sol.findMin([4,3]))
print (sol.findMin([1]))
