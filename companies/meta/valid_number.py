'''
LC 65: Valid Number
Given a string s, return whether s is a valid number.
For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", 
while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".
'''
class Solution:
    def isNumber(self, s: str) -> bool:
        digit, exponent, dot = False, False, False
        for i, c in enumerate(s):
            if c.isdigit():
                digit = True
            elif c in ['+', '-']:
                # A sign can either be the first character in a string
                # or should come right after an exponent sign
                if i > 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
            elif c in ['e', 'E']:
                # If exponent is seen, it should not be repeated 
                # and should come after digits
                if exponent or not digit:
                    return False
                exponent = True
                # We need to set this to false as e should be followed by
                # an integer, so we need to reset it again and recheck
                digit = False
            elif c == '.':
                # There can only be one dot in the string
                # and exponent should only be followed by an integer
                if dot or exponent:
                    return False
                dot = True
            else: # Any other character is invalid
                return False
        # We return digit since it is set to false after the exponent
        return digit

isValid = Solution().isNumber
print(isValid("0"))
print(isValid("e"))
print(isValid("."))
print(isValid("1.2e-10"))
print(isValid("1.2e-10.2"))
print(isValid("1.2ef-10.2"))