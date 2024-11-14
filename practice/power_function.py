'''
O(log(n)): We divide it by 2 each iteration
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            return 1.0/self.myPow(x, -n)
        if n % 2: 
            return x * self.myPow(x*x, (n-1)/2)
        else:
            return self.myPow(x*x, n/2)

print(Solution().myPow(2.00000, 10))
print(Solution().myPow(2.10000, 3))
print(Solution().myPow(2.00000, -2))
