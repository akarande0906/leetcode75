'''
LC 1768: Merge Strings Alternately
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
Input: word1 = "abc", word2 = "pqr" Output: "apbqcr"
Input: word1 = "abcd", word2 = "pq" Output: "apbqcd"
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_len = max(len(word1), len(word2))
        ret_arr = []
        for ptr in range(max_len):
            if ptr < len(word1):
                ret_arr.append(word1[ptr])
            if ptr < len(word2):
                ret_arr.append(word2[ptr])
        return ''.join(ret_arr)
                
merge = Solution().mergeAlternately
print (merge('abc', 'pqr'))
print (merge('ab', 'pqrs'))
print (merge('abcd', 'xy'))
