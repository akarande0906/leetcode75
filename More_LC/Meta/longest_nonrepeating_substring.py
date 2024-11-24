'''
LC 3: Given a string, find the longest non repeating substring
For example: abcabcbb => return abc or bca with length 3
bbbbbbb => return b with length 1
pwwkew => return wke or kwe with length of 3
'''
class Solution:
    def getLongestSubstring(self, string):
        max_len = 0
        lptr = 0
        rptr = 0
        visited = set()
        substring = ''
        while rptr < len(string):
            if not string[rptr] in visited:
                visited.add(string[rptr])
                max_len = rptr - lptr
                substring = string[lptr:rptr+1]
            else:
                while string[rptr] in visited:
                    visited.remove(string[lptr]) 
                    lptr += 1
                if string[rptr] not in visited:
                    visited.add(string[rptr])
            rptr += 1
        return substring

print (Solution().getLongestSubstring('abcabcbb'))
print (Solution().getLongestSubstring('bbbbbbb'))
print (Solution().getLongestSubstring('pwwkew'))
'''
adcdbcbb
  L
   R
'''                


