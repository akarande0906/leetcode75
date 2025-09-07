'''
LC 67: Add Binary
Given two binary strings a and b, return their sum as a binary string.
Input: a = "11", b = "1" Output: "100"
Input: a = "1010", b = "1011" Output: "10101"
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ptr1 = len(a) - 1
        ptr2 = len(b) - 1
        output = []
        while not (ptr1 < 0 and ptr2 < 0):
            x1 = ord(a[ptr1]) - ord('0') if ptr1 >= 0 else 0
            x2 = ord(b[ptr2]) - ord('0') if ptr2 >= 0 else 0
            sum = x1 ^ x2 ^ carry
            output.append(str(sum))
            carry = x1 + x2 + carry
            carry = 1 if carry > 1 else 0
            ptr1 -= 1
            ptr2 -= 1
        if carry:
            output.append(str(carry))
        output.reverse()
        return ''.join(output)

    ''' O(1) space solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ptr1 = len(a) - 1
        ptr2 = len(b) - 1
        output = ''
        while not (ptr1 < 0 and ptr2 < 0):
            x1 = ord(a[ptr1]) - ord('0') if ptr1 >= 0 else 0
            x2 = ord(b[ptr2]) - ord('0') if ptr2 >= 0 else 0
            sum = x1 ^ x2 ^ carry
            output = str(sum) + output
            carry = x1 + x2 + carry
            carry = 1 if carry > 1 else 0
            ptr1 -= 1
            ptr2 -= 1
        if carry:
            output = str(carry) + output
        return output
    '''
    


adder = Solution().addBinary
print (adder("11", "1"))
print (adder("1010", "1011"))
print (adder("1111", "1011"))
                

           

            