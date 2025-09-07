class Solution:
   def twoSum(self, nums: list[int], target: int) -> list[int]:
        id_map = {}
        n = len(nums)
        for lptr in range (0, n):
            if target - nums[lptr] in id_map:
                return [lptr, id_map[target-nums[lptr]]]
            id_map[nums[lptr]] = lptr
        return []
if __name__ == '__main__':
  print(Solution().twoSum([2,7,11,15], 9))
  print(Solution().twoSum([3,2,4], 6))
  print(Solution().twoSum([3,3], 6))


