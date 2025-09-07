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
    
    # Here we use the fact
    def kthfactor2(self, n: int, k: int) -> int:
        factor_count = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                factor_count += 1
                if factor_count == k:
                    return i
        
        if int(n**0.5) ** 2 == n:
            max_iter = int(n**0.5) - 1 # Perfect square case and therefore we can skip the square root as its already counter
        else:
            max_iter = int(n**0.5)
        
        for i in range(max_iter, 0, -1):
            if n % i == 0:
                factor_count += 1
                if factor_count == k:
                    return n // i  # here we return the reverse factor 
        return -1 # Not enough factors found

                
# Test cases for the kthFactor function

print (Solution().kthfactor2(12, 3))
print (Solution().kthfactor2(7, 2))
print (Solution().kthfactor2(22, 3))
