'''
LC 1726: Tuple with Same Product
'''
class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        # For any two pairs that match 
        # a*b = c*d will give us 8 combinations (ab = cd, ba=cd, ab=dc amd ba=dc)
        # For each pair product we can check the count and then use that to compute the 
        # final value : For each count of pairs > 1, we can use the formula ((v - 1) * v) // 2
        # to get the number of tuples that can be formed and multuply by 8
        pair_map = {}
        for i in range(len(nums) - 1):
            for j in range (i+1, len(nums)):
                prod = nums[i] * nums[j] 
                pair_map[prod] = pair_map.get(prod, 0) + 1
        num_tuples = 0
        for k, v in pair_map.items():
            if v > 1:
                factor = ((v - 1) * v) // 2
                num_tuples += factor * 8 
        return num_tuples

tupleSameProduct = Solution().tupleSameProduct
print(tupleSameProduct([2,3,4,6]))
print(tupleSameProduct([1,2,4,5,10]))
print(tupleSameProduct([2,3,4,6,8,12]))
print(tupleSameProduct([2,3,5,7]))

# Time Complexity : O(n^2)
# Space Complexity : O(n^2)