'''
LC 166: Fraction to Recurring Decimal
'''
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        fraction = []
        if numerator == 0:
            return '0'
        if numerator >= 0 and denominator < 0 or numerator < 0 and denominator >= 0:
            fraction.append('-')
        divd = abs(numerator)
        divs = abs(denominator)

        fraction.append(str(divd//divs))
        remainder = divd % divs
        if remainder == 0: 
            return ''.join(fraction)
        fraction.append('.')
        lookup = {}
        while remainder != 0:
            if remainder in lookup:
                fraction.insert(lookup[remainder], '(')
                fraction.append(')')
                break
            lookup[remainder] = len(fraction)
            remainder *= 10
            fraction.append(str(remainder//divs))
            remainder %= divs
        return ''.join(fraction)
            
# Time: O(n)
# Space: O(n)

fractionToDecimal = Solution().fractionToDecimal
print (fractionToDecimal(1, 7))
print (fractionToDecimal(1, 2))
print (fractionToDecimal(2, 1))
print (fractionToDecimal(2, 3))
print (fractionToDecimal(1, 6))
print (fractionToDecimal(-1, 7))
print (fractionToDecimal(0, -7))