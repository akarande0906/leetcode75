'''
LC 875: Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
Example 1: Input: piles = [3,6,7,11], h = 8 Output: 4
Example 2: Input: piles = [30,11,23,4,20], h = 5 Output: 30
Example 3: Input: piles = [30,11,23,4,20], h = 6 Output: 23
'''
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
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
    

minSpeed = Solution().minEatingSpeed
print (minSpeed([3,6,7,11], 8))
print (minSpeed([30,11,23,4,20], 5))
print (minSpeed([30,11,23,4,20], 6))