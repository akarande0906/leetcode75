'''
Leetcode 2571: Minimum Operations to Reduce integer to 0
'''
class Solution:
    def minOperations(self, n: int) -> int:
        # As n can be at max 99,999
        # We build powers till the nearest power of 2 that is 2^17
        powers = [2**num for num in range(18)]
        count = 0
        while n:
            for i in range(len(powers)):
                if powers[i] > n:
                    # Here we have found the nearest power of 2
                    break
            # Find the nearest power of 2 and update n
            n = min(abs(powers[i] - n), abs(powers[i-1] - n))
            count += 1
        return count

minOps = Solution().minOperations
print(minOps(99999))
print(minOps(39))
print(minOps(54))