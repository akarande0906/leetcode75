class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: 
            return True
        if num < 4:
            return False
        left = 1
        right = num // 2
        while left <= right:
            pivot = (right + left) // 2
            if pivot * pivot == num:
                return True
            elif pivot * pivot < num:
                left = pivot + 1
            else:
                right = pivot - 1
        return False


print (Solution().isPerfectSquare(16))
print (Solution().isPerfectSquare(256))
print (Solution().isPerfectSquare(2000105819))
