class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_num = 0
        for i in range(32):
            reversed_num = (reversed_num << 1) |  (n & 1)
            n >>= 1
        return reversed_num

sol = Solution()
print(bin(sol.reverseBits(21)))
print(bin(sol.reverseBits(4294967293)))
print(bin(sol.reverseBits(43261596)))
