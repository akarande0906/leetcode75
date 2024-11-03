class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            k = i + 2
            if nums[i]:
                for j in range(i+1, len(nums) - 1):
                    while (k < len(nums) and nums[i] + nums[j] > nums[k]):
                        k += 1
                    count += k - j - 1
        return count

print(Solution().triangleNumber([4,2,3,4]))
print(Solution().triangleNumber([2,2,3,4]))
print(Solution().triangleNumber([2,2,1,0]))
