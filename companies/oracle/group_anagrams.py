'''
LC 49: Group Anagrams
'''
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
    

# Time Complexity: O(n * k log k) where n is the number of strings and k is the maximum length of a string.
# Space Complexity: O(n * k) for storing the anagrams in the dictionary.
sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(sol.groupAnagrams([""])) # [['']]
print(sol.groupAnagrams(["a"])) # [['a']]
print(sol.groupAnagrams(["abc", "bca", "cab", "xyz"])) # [['abc', 'bca', 'cab'], ['xyz']]
            