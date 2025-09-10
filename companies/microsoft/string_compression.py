'''
Leetcode 443: 
'''
from typing import List


class Solution:

    def compress(self, chars: List[str]) -> int:

        def addEncodedChars(char, length):
            nonlocal lptr
            chars[lptr] = cur_char
            lptr += 1
            if cur_len > 1:
                chars[lptr] = str(cur_len)
                lptr += 1


        lptr = 0
        cur_char, cur_len = chars[0], 1
        for rptr in range(1, len(chars)):
            if chars[rptr] == cur_char:
                cur_len += 1
            else:
                addEncodedChars(cur_char, cur_len)
                cur_char, cur_len = chars[rptr], 1
        addEncodedChars(cur_char, cur_len)
        print (chars[0:lptr])
        return lptr
    
compress = Solution().compress
print(compress(["a","a","b","b","c","c","c"]))
print(compress(["a"]))
print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))

   

        
