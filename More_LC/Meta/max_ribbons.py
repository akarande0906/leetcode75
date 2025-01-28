'''
LC 1891: Cutting Ribbons
'''
class Solution:
    def maxLength(self, ribbons: list[int], k: int) -> int:
        left, right = 1, max(ribbons)
        def isOk(index):
            total_ribbons = 0
            for ribbon in ribbons:
                total_ribbons += ribbon // index
                if total_ribbons >= k:
                    return True
            return False
        max_len = 0
        while left <= right:
            mid = (left + right) // 2
            if isOk(mid):
                max_len = mid
                left = mid + 1
            else:
                right = mid - 1
        return max_len

# Time Complexity: O(NlogM) where N is the number of ribbons and M is the maximum length of the ribbons
# Space Complexity: O(1) since we are not using any extra space

finder = Solution().maxLength
print(finder([1,2,3,4,5,6,7,8,9], 5)) # 4
print(finder([5,7,8], 5)) # 6
print(finder([1,2,3,4,5,6,7,8,9], 5)) # 4
print(finder([7,8,9], 30)) 