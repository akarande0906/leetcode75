''' LC 219 '''
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        diff_map = {}
        for n in range(len(nums)):
            if nums[n] in diff_map:
                diff_map[nums[n]] = abs(diff_map[nums[n]] - n)
                if diff_map[nums[n]] <= k:
                    return True
            diff_map[nums[n]] = n
        return False  

print (Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2))
print (Solution().containsNearbyDuplicate([1,0,1,1], 1))
