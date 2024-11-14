class Solution:
    def maxProduct(self, A):
        if not A: 
            return 0
        minProd = A[0]
        maxProd = A[0]
        result = A[0]
        for i in range(1, len(A)):
            if  A[i] < 0:
                minProd, maxProd = maxProd, minProd
            maxProd = max(A[i] * maxProd, A[i])
            minProd = min(A[i] * minProd, A[i])
            result = max(maxProd, result)
        return result


print (Solution().maxProduct([2, 3, -2, 4]))
print (Solution().maxProduct([-2,0,-1]))
                
        
