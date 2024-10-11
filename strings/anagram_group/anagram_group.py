'''
LT 49: Group anagrams: Given an array of strings strs, group the anagrams together. You can return the answer in any order.
'''
from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
   anagram = defaultdict(list)
   for s in strs:
      sort_s = ''.join(sorted(s))
      anagram[sort_s].append(s)
   
   return list(anagram.values())


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
      

