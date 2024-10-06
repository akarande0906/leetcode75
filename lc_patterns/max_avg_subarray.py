'''
Prob: 643
'''
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        lptr = 0
        ps = set()
        total = 0
        max_tot = float('-inf')
        for i in range(len(nums)):
              total += nums[i]
              if i - lptr + 1 == k:
                 max_tot = max(total, max_tot)
                 total -= nums[lptr]
                 lptr += 1
        return max_tot/k

print(Solution().findMaxAverage([1,12,-5,-6,50,3],4))
