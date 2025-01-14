'''
LC 125: Valid Palindrome
'''
class Solution:
    def isValidPalindrome(self, s):
        ''' Short Cut 
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        return s == s[::-1]
        '''
        if len(s) == 1:
            return True
        p = 0
        r = len(s) - 1
        while p <= r:
            while not s[p].isalnum():
                p += 1
            while not s[r].isalnum():
                r -= 1
            if s[p].lower() != s[r].lower():
                return False
            p += 1
            r -= 1
        return True

isValid = Solution().isValidPalindrome
print(isValid("A man, a plan, a canal: Panama"))
print(isValid("race a car"))
print(isValid(" "))
