'''
LC 2303: Calculate Amount in Taxes
'''
class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        tax = 0.0
        b_income = 0
        for b in brackets:
            b_income = min(b[0] - b_income, income)
            tax += b_income * b[1] / 100
            income -= b_income
            b_income = b[0]
        return tax
    
calculateTax = Solution().calculateTax
print(calculateTax([[3,50],[7,10],[12,25]], 10))
print(calculateTax([[1,0],[4,25],[5,50]], 2))
print(calculateTax([[2,50]], 0))
print(calculateTax([[2,50]], 1))
print(calculateTax([[2,7],[3,17],[4,37],[7,6],[9,83],[16,67],[19,29]], 18))

# Time Complexity : O(n)
# Space Complexity : O(1)

            