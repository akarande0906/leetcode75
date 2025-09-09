'''
Leetcode 69: Square root of a number without using Python operators
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        # We can use binary search here 
        # Alternative is to go from 2 to the number by 2 till we find the square root
        # But that will result in O(n/2) or O(n) time.

        left, right = 1, x // 2 # Narrow the search here 
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x: # Perfect square
                return mid
            else:
                if mid * mid > x: 
                    right = mid - 1
                else:
                    left = mid + 1
        return right # Because we are looking for the nearest number to the left
        

sqr = Solution().mySqrt
print(sqr(99))
print(sqr(16))
print(sqr(8))
print(sqr(100))
                