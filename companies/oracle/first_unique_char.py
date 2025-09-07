'''
LC: 387: First Unique Char in String
'''
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for idx in range(len(s)):
            chr = s[idx]
            if cnt[chr] == 1:
                return idx
        return -1

sol = Solution()
print(sol.firstUniqChar('leetcode'))
print(sol.firstUniqChar('loveleetcode'))
print(sol.firstUniqChar('aabb'))
