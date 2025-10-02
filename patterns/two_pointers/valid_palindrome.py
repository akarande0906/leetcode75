'''
Leetcode 125: Valid Palindrome
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (''.join(ch.lower() for ch in s if ch.isalnum()))
        return s == s[::-1]
    
    def isPalindrome2(self, s: str) -> bool:
        s = s.lower()
        lptr, rptr = 0, len(s) - 1
        while lptr <= rptr:
            while not s[lptr].isalnum() and lptr < len(s):
                lptr += 1
            while not s[rptr].isalnum() and rptr > -1:
                rptr -= 1
            if s[lptr] != s[rptr]:
                return False
            lptr += 1
            rptr -= 1
        
        return True
    

pal = Solution().isPalindrome2
print(pal("Was it a car or a cat I saw?"))
print(pal("tab a cat"))
print(pal("Madam I'm Adam"))
print(pal("Mada3 1'3 Adam"))