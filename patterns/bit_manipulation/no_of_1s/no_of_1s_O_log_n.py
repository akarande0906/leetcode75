class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            n = n & (n -1)
            count += 1
        return count     


sol = Solution()
print(sol.hammingWeight(10))
print(sol.hammingWeight(15))

