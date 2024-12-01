'''
LC 989: Add to Array-form of Integer
The array-form of an integer num is an array representing its digits in left to right order.
For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
Example: Input: num = [1,2,0,0], k = 34 Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
'''
class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        sum_array = []
        n = len(num) - 1
        carry = 0
        while True:
            if n < 0 and k <= 0:
                break
            cur_sum = carry
            cur_sum += num[n] if n >= 0 else 0
            cur_sum += k % 10 if k >= 0 else 0
            carry = cur_sum // 10 
            cur_sum = cur_sum % 10 
            sum_array.append(cur_sum)
            n -= 1
            k = k // 10
        sum_array.reverse()
        if carry:
            sum_array = [carry] + sum_array
        return sum_array

adder = Solution().addToArrayForm
print (adder([2,1,5], 806))
print (adder([2,7,4], 181))
print (adder([1,2,0,0], 34))
            