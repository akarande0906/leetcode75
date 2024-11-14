'''
Implement pow(x, n) % d.

Note that remainders on division cannot be negative.
In other words, make sure the answer you return is non-negative.

For example:
    x= 2, n = 3, d = 3: Sol = 2
    x= 5, n = 2, d = 6: Sol = 1
'''

class Solution:
    def pow(self, a, y, d): 
        if a == 0:
            return 0
        res = 1
        while y > 0:
            if y % 2:
                res = (res * a) % d
            y = y // 2
            a = (a*a) % d
        return (d + res) % d

print (Solution().pow(2, 3, 2))
print (Solution().pow(5, 2, 6))

