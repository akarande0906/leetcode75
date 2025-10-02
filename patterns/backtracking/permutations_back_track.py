# 46: Permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [nums[:]]  # Return array with one element
        res = []

        for _ in range(len(nums)):
            n = nums.pop(0)
            print (n)
            perm = self.permute(nums)
            for p in perm:
                print (p)
                p.append(n)
            res.extend(perm)
            print (res)
            nums.append(n)
        return res


print (Solution().permute([1,2,3]))
