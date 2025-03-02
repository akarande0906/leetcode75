'''
LC 9: Palindrome Number
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        if x == 0:
            return True
        num_str = str(x)
        lptr, rptr = 0, len(num_str) - 1
        if lptr == rptr:
            return True
        while lptr < rptr:
            if num_str[lptr] != num_str[rptr]:
                return False
            lptr += 1
            rptr -= 1
        return True

    # TC : O(n)
    # SC : O(1)
    
    def isPalindrome_v2(self, x: int) -> bool:
        if x < 0: 
            return False
        if x == 0:
            return True
        # Find number of digits
        lnum = x
        ndigs = 0
        while lnum:
            lnum = lnum // 10
            ndigs += 1 
        lnum, rnum = x, x
        while lnum and rnum:
            ldig = lnum // (10 ** (ndigs - 1))
            lrem = lnum % (10 ** (ndigs - 1))
            rdig = rnum % 10
            rrem = rnum // 10
            if ldig != rdig:
                return False
            lnum, rnum, ndigs = lrem, rrem, ndigs - 1

        return True
    
    # TC : O(log10(n))
    # SC : O(1)
    

isPalindrome = Solution().isPalindrome_v2
print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
print(isPalindrome(-101))