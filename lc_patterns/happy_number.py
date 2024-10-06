# No: 202

class Solution:
    def isHappy(self, n: int) -> bool:
        number = 0
        numbers = set()
        c_num = n

        while True:
            for i in str(c_num):
                number += int(i) ** 2
            if number == 1:
                return True
            if number in numbers:
                return False
            numbers.add(number)
            c_num = number
            number = 0

sol = Solution()
print(sol.isHappy(19))
print(sol.isHappy(2))
print(sol.isHappy(10))
print(sol.isHappy(18))
