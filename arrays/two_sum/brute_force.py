class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for lptr in range (0, len(nums) - 1):
            for  rptr in range(lptr+1, len(nums)):
                if nums[lptr] + nums[rptr] == target:
                    return [lptr, rptr]
        return []


if __name__ == '__main__':
  print(Solution().twoSum([2,7,11,15], 9))
  print(Solution().twoSum([3,2,4], 6))
  print(Solution().twoSum([3,3], 6))
