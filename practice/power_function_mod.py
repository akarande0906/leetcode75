'''
O(log(n)): We divide it by 2 each iteration

Note: To compute x^y mod d => (x mod d) ^ y mod d
To compute power recursively: x ^ y = (x*x) ^ y/2 if even, x * (x*x) ^ (y-1)/2
'''

class Solution:
    def myPow(self, x: int, n: int, d: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            if n < 0:
                return 1/helper(x, -n)
            if n % 2: 
                return x * helper(x*x, (n-1)/2)
            else:
                return helper(x*x, n/2)
        val = helper(x % d, n)
        return val % d

print(Solution().myPow(2, 3, 3))
print(Solution().myPow(5, 2, 6))
print(Solution().myPow(9, 5, 7))
print(Solution().myPow(-9, 5, 7))
