'''
LC 66: Plus One
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
Example: Input: digits = [9] Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
'''
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        for dig in range(n-1, -1, -1):
            if digits[dig] != 9:
                digits[dig] += 1
                return digits
            digits[dig] = 0
        return [1] + digits

adder = Solution().plusOne
print (adder([9,9]))
print (adder([1, 2, 3]))
print (adder([1, 9, 9]))
print (adder([4, 3, 2, 1]))
