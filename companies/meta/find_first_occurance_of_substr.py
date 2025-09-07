'''
LC 28: Find First Occurance of Substring
Given two strings needle and haystack, return the index of the 
first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if n > len(haystack):
            return -1
        i = 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]: # Start of the string
                if i + len(needle) > len(haystack):
                    return -1
                else:
                    if haystack[i:i+n] == needle:
                        return i
        return -1
        
# Time Complexity: O(NM) where N is the number of elements in the haystack, 
# M is the number of elements in the needle.
# Space Complexity: O(1) as we are using only a constant space

print (Solution().strStr("hello", "ll")) # 2
print (Solution().strStr("aaaaa", "bba")) # -1
print (Solution().strStr("leetcode", "leet")) # 0
print (Solution().strStr("leetcode", "leeto")) 