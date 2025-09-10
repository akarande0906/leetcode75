'''
Leetcode 46: Permutations
'''
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm_array = []

        def permute(curr):
            if len(curr) == len(nums):
                perm_array.append(curr[:])
                return

            for num in nums:
                # This condition ensures that on recursive call we dont add the same element again
                if num not in curr: 
                    # Backtrack
                    curr.append(num)
                    permute(curr)
                    curr.pop()
        ans = []
        permute([])
        return perm_array

perm = Solution().permute
print(perm([1,2,3]))
print(perm([0,1]))
print(perm([3]))

# Time complexity: O(n . n!): n! for the permutations, n for the copy of curr
# Space Complexity: O(n): Space for the recursion stack
