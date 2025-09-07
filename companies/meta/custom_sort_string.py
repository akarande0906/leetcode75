'''
LC: 791: Custom Sort String
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
Permute the characters of s so that they match the order that order was sorted. 
More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
Return any permutation of s that satisfies this property.
'''

from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        map = defaultdict(int)
        for c in s:
            map[c] += 1
        sorted_str = ''
        for c in order:
            if c in map:
                sorted_str += c * map[c]
                del map[c]
        for c in map:
            sorted_str += c * map[c]
        return sorted_str

print (Solution().customSortString('bcafg', 'abcd'))
print (Solution().customSortString('cba', 'abcd'))
print (Solution().customSortString('huvw', 'hfhgjdhtuwetowiptireptoejgkjfd3hryewirworewurouwerabcabcacbqqmz'))