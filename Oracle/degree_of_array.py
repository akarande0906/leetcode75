'''
LC 697: Degree of an Array
'''
class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        left, right, count = {}, {}, {}
        for i, n in enumerate(nums):
            if not n in left:
                left[n] = i #Left most occurence of n
            right[n] = i # Right most occurence of n
            count[n] = count.get(n, 0) + 1 # Count of n in nums
        
        # Now find the degree of n
        degree = max(count.values())
        ans = len(nums) # Default
        for c in count:
            if count[c] == degree:
                ans = min(ans, right[c] - left[c] + 1)
        return ans

# Time: O(n)
# Space: O(n)
findShortestSubArray = Solution().findShortestSubArray
assert findShortestSubArray([1, 2, 2, 3, 1]) == 2
assert findShortestSubArray([1, 2, 2, 3, 1, 4, 2]) == 6
assert findShortestSubArray([1,2,2,3,1,4,2]) == 6
