class Solution:
    def getMaxXor(self, nums: list[int], maxBit: int) -> list[int]:
        xor = 0
        for n in nums:
            xor ^= n
        mask = (1 << maxBit) - 1
        answer = []
        for n in reversed(nums):
            answer.append(xor ^ mask)
            xor ^= n
        return answer


print (Solution().getMaxXor([0,1,1,3], 2))

'''
max value: 2**2 = 4 => 100 - 1 = 11
1 << 2 - 1 = 11
xor = 11
mask = 11
'''
