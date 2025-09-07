class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len (nums)
        ans = []
        nums.sort()
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0: # It means that you need a bigger j
                    j+= 1
                elif sum > 0: # It means you need a smaller k
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j+= 1
                    while j < k and nums[k] == nums[k+1]:
                        k-= 1
        return ans
        

sol = Solution()
print (sol.threeSum([-1,0,1,2,-1,-4]))
print (sol.threeSum([0,1,1]))
print (sol.threeSum([0,0,0]))
print (sol.threeSum([-1,0,1,2,-1,-1,-4]))
