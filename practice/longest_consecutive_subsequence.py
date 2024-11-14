'''
LC: 128
'''

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        unique_elems = set(nums)
        max_len = 0
        n = len(nums)
        for num in unique_elems:
            cur_len = 1
            if num - 1 not in unique_elems: # Start of a sequence
                while num+cur_len in unique_elems:
                    cur_len += 1
            max_len = max(cur_len, max_len)
        return max_len

print (Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
