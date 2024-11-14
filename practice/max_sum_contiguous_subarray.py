class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return 0
        currentTotal = A[0]
        maxTotal = A[0]
        for i in range(1,len(A)):
            currentTotal += A[i]
            if currentTotal < 0:
                currentTotal = 0
            maxTotal = max(maxTotal, currentTotal)
        return maxTotal   

print (Solution().maxSubArray([1, 2, 3, 4, -10]))
print (Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
                
