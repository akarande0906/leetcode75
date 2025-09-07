''' LC 213: House Robber II: House robber with houses in a circle
'''

class Solution:
    '''
    Break this into two partial problems:
    First one excluding last house
    Second one excluding the first house
    and find the max
    ''' 
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        temp_nums = nums.copy()
        nums[1] = max(nums[0], nums[1] if len(nums) > 1 else 0)
        for house in range(2, len(nums) - 1): # Skip last house
            nums[house] = max(nums[house] + nums[house - 2], nums[house - 1])
        cur_max = nums[-2]
        nums = temp_nums
        nums[len(nums) - 2] = max(nums[len(nums) - 1], nums[len(nums) - 2]) # Skip first house
        for house in range(len(nums) - 3, 0, -1):
            nums[house] = max(nums[house] + nums[house + 2], nums[house + 1])
        return max (cur_max, nums[1])
