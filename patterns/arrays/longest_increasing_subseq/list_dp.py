class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        max_val = 0
        final_res = [1] * len(nums)
        max_seq = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    final_res[i] = max(final_res[j] + 1, final_res[j])
                    max_seq = max(max_seq, final_res[i])
        print (max_seq)
        return max(final_res)


print(Solution().lengthOfLIS([1,2,3,0,1,2,3]))
                    
