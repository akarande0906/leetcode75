''' Leet Code: 136 '''
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        fin = 0
        for n in nums:
            fin = fin ^ n
        return fin

print (Solution().singleNumber([2,2,1]))
print (Solution().singleNumber([4,1,2,1,2]))
print (Solution().singleNumber([1]))
