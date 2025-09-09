'''
Leetcode 7: Reverse Integer
'''
class Solution:
    def reverseInteger(self, x: int) -> int:
        if x >= -9 and x <= 9:
            return x
        is_neg = True if x < 0 else False
        x = abs(x)
        rev_int = 0
        while x:
            rev_int = rev_int * 10 + x % 10
            x = x // 10
        if is_neg:
            rev_int = -rev_int
        if rev_int > 2 ** 31 - 1 or rev_int < -2 ** 31:
            return 0
        return rev_int
    
rev = Solution().reverseInteger
print(rev(123))
print(rev(-349))
print(rev(120))
[print(rev(-6))]
