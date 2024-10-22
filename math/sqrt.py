class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: 
            return 1
        for i in range(x//2, 1, -1):
            if i*i == x:
                return i
            elif i*i < x:
                return i

print(Solution().mySqrt(8))
print(Solution().mySqrt(16))
print(Solution().mySqrt(256))
print(Solution().mySqrt(1000))
