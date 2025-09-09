'''
Leetcode 383: Ransom Note
'''
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count the characters in ransomNote
        c = Counter(ransomNote)
        for l in magazine:
            if l in c and c[l]:
                c[l] -= 1
                if c[l] < 0:
                    return False
        used = sum(c.values()) == 0
        return used

con = Solution().canConstruct
print(con('a', 'b'))
print(con('aa', 'ab'))
print(con('aa', 'aab'))
print(con('bg', 'efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj'))