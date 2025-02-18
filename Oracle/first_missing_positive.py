'''
LC 41: First Missing Positive
'''
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        min_val = float('inf')
        max_val = float('-inf')
        n = len(nums)
        i = 0
        # Cycle sort the array
        while i < n:
            real_id = nums[i] - 1 # Right index where this num should be
            # If the number is not at the right index swap it with the 
            # number at that index
            if 0 < nums[i] <= n and nums[i] != nums[real_id]:
                nums[i], nums[real_id] = nums[real_id], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
# Time: O(n)
# Space: O(1)
first_missing = Solution().firstMissingPositive
assert first_missing([1,2,0]) == 3
assert first_missing([3,4,-1,1]) == 2
assert first_missing([7,8,9,11,12]) == 1
assert first_missing([1,2,3]) == 4
assert first_missing([1,2,3,4]) == 5
            
            

        