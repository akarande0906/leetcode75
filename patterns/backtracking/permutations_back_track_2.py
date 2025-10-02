class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def permutation(i):
            if i == len(nums):
                sl = nums
                res.append(sl.copy())
                
            for j in range (i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                print (str(nums) + ' -> i: ' + str(i) + ', j: ' + str(j))
                permutation(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        permutation(0)
        return res

print(Solution().permute([1, 2, 3]))
