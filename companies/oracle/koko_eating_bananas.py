'''
LC 875: Koko Eating Bananas
'''
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Here we need to do a binary search to find the optimal solution
        # because the slowest we can go is 1 banana an hour and the fastest
        # we can go is max(piles) per hour - anything greater than that will give
        # same result as max(piles). We dont have to sort because we are using binary
        # search to opmtimize k and not find a value within the pile
        def computeHours(piles, mid):
            hours = 0
            for p in piles:
                hours += p // mid
                if p % mid: # if there is a remainder add another hour
                    hours += 1
            return hours
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            hours = computeHours(piles, mid)
            if hours <= h: 
                # Here we still try to optimize for a slower value 
                high = mid
            else:
                low = mid + 1
        return low
# Time Complexity: O(n log m) where n is the number of piles and m is the maximum number of bananas in a pile.
# Space Complexity: O(1) since we are not using any extra space other than a few variables.
sol = Solution()
print(sol.minEatingSpeed([3,6,7,11], 8))  # 4
print(sol.minEatingSpeed([30,11,23,4,20], 5))  # 30
print(sol.minEatingSpeed([30,11,23,4,20], 6))  # 23