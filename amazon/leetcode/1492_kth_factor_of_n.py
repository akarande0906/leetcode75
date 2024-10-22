class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [1]
        start = 2
        if n % 2 != 0:
            start += 1
        for fact in range (start, n//2 + 1):
            #print (factors)
            if n % fact == 0:
                factors.append(fact)
            if len(factors) == k:
                return factors[k-1]
        if len(factors) == k - 1:
            return n
        return -1 

print (Solution().kthFactor(12, 3))
print (Solution().kthFactor(7, 3))
print (Solution().kthFactor(22, 3))
