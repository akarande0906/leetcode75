'''
LC 680: Valid Palindrome II: 
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        if s == s[::-1]:
            return True
        else:
            lptr = 0
            rptr = len(s) - 1
            dels = 0
            while lptr <= rptr:
               
                if s[lptr] != s[rptr]:
                    return checkPalindrome(s, lptr + 1, rptr) or checkPalindrome(s, lptr, rptr - 1)
                lptr += 1
                rptr -= 1
               
            return True

isPalindrome = Solution().validPalindrome
print (isPalindrome('aba'))
print (isPalindrome('abca'))
print (isPalindrome('aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga'))
print (isPalindrome('abcde'))
