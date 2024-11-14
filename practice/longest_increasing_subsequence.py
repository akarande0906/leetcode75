import bisect

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n # As for each element by itself it can be seq of 1
        # See if we can keep adding to the sequence
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS2(self, nums: list[int]) -> int:
        sub = []
        for num in nums:
            i = bisect.bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num
        
        return len(sub)
        

print (Solution().lengthOfLIS2([10,9,2,5,3,7,101,18]))
print (Solution().lengthOfLIS2([0,1,0,3,2,3]))

