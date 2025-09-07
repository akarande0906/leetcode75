'''
LC 525: Contiguous Array
'''
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        count_map = {0:-1}
        curr_count = 0
        max_len = 0
        for i, n in enumerate(nums):
            curr_count = curr_count + 1 if n else curr_count - 1
            if curr_count in count_map:
                max_len = max(max_len, i - count_map[curr_count])
            else:
                count_map[curr_count] = i
        return max_len  
            
# Time: O(n)
# Space: O(n)
max_len = Solution().findMaxLength
assert max_len([0,1]) == 2
assert max_len([0,1,0]) == 2
assert max_len([0,1,0,1]) == 4
assert max_len([0,1,1,0,1,1,1,0]) == 4
assert max_len([1,0,1,0,1,0,1,1,1]) == 6