'''
LC 1137: N-th Tribonacci Number
'''
class Solution:
    def tribonacci(self, n: int) -> int:
        first = 0
        second = 1
        third = 1
        if n == 0:
            return first
        if n == 1:
            return first + second
        for i in range(2, n):
            first, second, third = second, third, first+second+third
        return third
            
trib = Solution().tribonacci
print(trib(4))
print(trib(25))
print(trib(37))

# TC : O(N)
# SC : O(1)
