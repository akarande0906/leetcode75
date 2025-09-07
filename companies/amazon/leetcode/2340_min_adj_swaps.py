class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        min, min_id = float('inf'), -1
        max, max_id = 0, -1
        swaps = 0
        for index, num in enumerate(nums):
            if num < min:
                min = num
                min_id = index
            if num >= max:
                max = num
                max_id = index
        if min_id < max_id:
            swaps = min_id + len(nums) - max_id - 1
        else:
            swaps = min_id + len(nums) - max_id - 2
        return swaps


print (Solution().minimumSwaps([3,4,5,5,3,1]))
print (Solution().minimumSwaps([2,1]))
