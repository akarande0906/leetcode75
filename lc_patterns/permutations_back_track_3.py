class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        templist = []
        def permutation():
            if len(templist) == len(nums):
                res.append(templist.copy())
                return
            for j in range (0, len(nums)):
                if nums[j] in templist:
                    print ('Continue : ' + str(nums[j]))
                    continue 
                templist.append(nums[j])
                print ('Before: ' + str(templist))
                permutation()
                print ('After: ' + str(templist))
                templist.pop()

        permutation()
        return res

print(Solution().permute([1, 2, 3]))
#print(Solution().permute([1, 2, 3,4]))
