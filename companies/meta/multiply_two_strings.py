'''
LC 43: Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
Example 1: Input: num1 = "2", num2 = "3" Output: "6"
Example 2: Input: num1 = "123", num2 = "456" Output: "56088"
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        # create result array with max of 
        n = len(num1) + len(num2)
        answer = [0] * n

        first_num = num1[::-1]
        second_num = num2[::-1]

        for place2, digit2 in enumerate(second_num):
            for place1, digit1 in enumerate(first_num):
                cur_carry_id = place1 + place2
                carry = answer[cur_carry_id]
                product = int(digit1) * int(digit2) + carry
                # Store the digit from the product
                answer[cur_carry_id] = product % 10
                answer[cur_carry_id + 1] += product // 10
        if answer[-1] == 0:
            answer.pop()

        return ''.join(str(digit) for digit in reversed(answer))  

            
mul = Solution().multiply
print (mul('2', '3'))
print (mul('123', '456'))
print (mul('999', '999'))