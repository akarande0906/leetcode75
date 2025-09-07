class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        left = 0
        n = len(s)
        chars = set()
        for right in range(n):
            if s[right] not in chars:
                chars.add(s[right])
                maxLen = max(maxLen, right-left+1)
            else:
                while s[right] in chars:
                    chars.remove(s[left])
                    left += 1
                chars.add(s[right])
        return maxLen

sol = Solution()
print(sol.lengthOfLongestSubstring('abcabcbb'))
print(sol.lengthOfLongestSubstring('pwwkew'))
