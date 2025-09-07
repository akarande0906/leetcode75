'''
LC 340: Longest Substring with At Most K Distinct Characters
'''
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        map = {}
        left = 0
        max_len = 0
        dist_count = 0
        max_count = 0
        for right in range(len(s)):
            if not s[right] in map or map[s[right]] == 0:
                dist_count += 1
                if dist_count > k:
                    while dist_count > k:
                        map[s[left]] -= 1
                        if map[s[left]] == 0:
                            dist_count -= 1
                        left += 1
                
            map[s[right]] = map.get(s[right], 0) + 1
            max_count = max(max_count, right - left + 1)
        return max_count
                
# Time: O(n)
# Space: O(k) 
lengthOfLongestSubstringKDistinct = Solution().lengthOfLongestSubstringKDistinct
assert lengthOfLongestSubstringKDistinct("eceba", 2) == 3
assert lengthOfLongestSubstringKDistinct("aa", 1) == 2
assert lengthOfLongestSubstringKDistinct("a", 1) == 1
assert lengthOfLongestSubstringKDistinct("a", 0) == 0
assert lengthOfLongestSubstringKDistinct("aba", 1) == 1
assert lengthOfLongestSubstringKDistinct("aac", 1) == 2
