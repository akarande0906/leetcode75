'''
LC 567: Permutation in String
'''
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, word_len = Counter(s1), len(s1)

        for i in range(len(s2)):
            if s2[i] in cntr:
                cntr[s2[i]] -= 1
            if i >= word_len and s2[i-word_len] in cntr:
                cntr[s2[i-word_len]] += 1
            
            if all([cntr[i] == 0 for i in cntr]):
                return True
        return False
# Time: O(n)
# Space: O(n) # For the counter

checkInclusion = Solution().checkInclusion
assert checkInclusion("ab", "eidbaooo") == True
assert checkInclusion("ab", "eidboaoo") == False
assert checkInclusion("adc", "dcda") == True
assert checkInclusion("hello", "ooolleoooleh") == False
assert checkInclusion("hello", "ooolleoolleh") == True

                