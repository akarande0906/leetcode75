'''
LC 12: Integer to Roman
Given an integer, convert it to a roman numeral.
'''
digits = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_str = []
        for value, symbol in digits:
            if num == 0:
                break
            # Get the quotient and remainder when we divide the number by value
            count, num = divmod(num, value)
            roman_str.append(symbol * count)
        return ''.join(roman_str) 

itor = Solution().intToRoman
print(itor(3749))
print(itor(3))
print(itor(58))
print(itor(1994))
print(itor(3999))

# Time Complexity: O(1) as we are only iterating over a fixed number of elements
# Space Complexity: O(1) as we are only storing constant values in the list and no extra space is used


        