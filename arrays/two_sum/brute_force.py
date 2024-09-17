class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for lptr in range (0, len(nums) - 1):
            for  rptr in range(lptr+1, len(nums)):
                if nums[lptr] + nums[rptr] == target:
                    return [lptr, rptr]
        return []


if __name__ == '__main__':
  print(twoSum([2,7,11,15], 9)
  print(twoSum([3,2,4], 6)
