class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        id_map = {}
        for lptr in range (1, len(nums)):
            id_map[nums[lptr]] = lptr
        for lptr in range (0, len(nums) - 1):
            if target - nums[lptr] in id_map and id_map[target-nums[lptr]] != lptr:
                return [lptr, id_map[target-nums[lptr]]]
        return []

if __name__ == '__main__':
  print(Solution().twoSum([2,7,11,15], 9))
  print(Solution().twoSum([3,2,4], 6))
  print(Solution().twoSum([3,3], 6))


