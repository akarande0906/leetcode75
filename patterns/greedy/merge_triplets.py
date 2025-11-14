'''
Leetcode 1899: Merge triplets to form target triplets
'''
from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Find all triplets where values are greater at any position 
        # than the target. If so this triplet cannot be part of the solution.
        good_pos = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                # Not a valid triplet
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    # Since we have eliminated all triplets with values 
                    # greater than the sum, the equal value will always be
                    # the max when comparing with another triplet.
                    good_pos.add(i)
        # If we get matches for all three positions
        return len(good_pos) == 3
    

merger = Solution().mergeTriplets
print(merger([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]))
print(merger([[3,4,5],[4,5,6]], [3,2,5]))

# Time Complexity: O(n), Space Complexity: O(1) since our good_pos set is only len of 3 at max
