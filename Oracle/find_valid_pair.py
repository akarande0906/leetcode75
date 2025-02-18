'''
LC 3438: Find Valid Pair
'''

from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
        ctr = dict(Counter(s))
        for id in range(1, len(s)):
            if s[id] != s[id - 1]:
                if str(ctr[s[id]]) == s[id] and str(ctr[s[id-1]]) == s[id-1]:
                    return s[id-1:id+1]
        return ''
# Time: O(n)
# Space: O(n) for the Counter/dict
findValidPair = Solution().findValidPair
print (findValidPair("1122"))
print (findValidPair("1234"))
print (findValidPair("1221"))
print (findValidPair("2523533"))
print (findValidPair("221"))


    