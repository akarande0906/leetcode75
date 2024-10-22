class Solution:
   def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

sol = Solution()
print (sol.findMin([4,5,6,0,1,2,3]))
print (sol.findMin([3,4,5,1,2]))
print (sol.findMin([4,5,6,7,0,1,2]))
print (sol.findMin([6,7,0,1,2,3,4]))
print (sol.findMin([11,13,15,17]))
print (sol.findMin([4,3]))
print (sol.findMin([1]))
