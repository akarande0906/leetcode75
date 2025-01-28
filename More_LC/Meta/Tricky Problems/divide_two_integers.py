'''
LC 29: Divide Two Integers
Given two integers dividend and divisor, divide two integers 
without using multiplication, division, and mod operator.
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        HALF_MIN_INT = -1073741824
        
        # Special case to avoid overflow
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor
        
        powerOfTwo = 1
        doubles = []
        powersOfTwo = []
        while divisor >= dividend: # Remember we are working with negative numbers
            doubles.append(divisor)
            powersOfTwo.append(powerOfTwo)
            if divisor < HALF_MIN_INT:
                # When we reach this limit 
                break 
            divisor += divisor
            powerOfTwo += powerOfTwo
        
        # Now lets try to add the power value of divisor and see if its within the value
        quotient = 0
        for i in reversed(range(len(doubles))):
            if doubles[i] >= dividend: # If it fits, add it
                quotient += powersOfTwo[i]
                dividend -= doubles[i]
        # If we have exactly one negative it means one of the dividend/divisor is 
        # negative, so the answer will be negative
        return quotient if negatives != 1 else -quotient

# Time Complexity: O(logN) where N is the dividend
# Space Complexity: O(logN) as we are using a list of size logN

print (Solution().divide(10, 3)) # 3
print (Solution().divide(7, -3)) # -2
print (Solution().divide(12345, 3)) # 4115
