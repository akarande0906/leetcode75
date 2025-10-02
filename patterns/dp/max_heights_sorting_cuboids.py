'''
Leetcode 1691: Maximum Height by Stack Cuboids
'''
from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # First sort the boxes such that the dimensions are sorted
        for c in cuboids:
            c.sort()
        # Now sort them in ascending order of the lowest dimension
        cuboids.sort()
        # Sort by descending dimensions
        # cuboids.sort(key=lambda x: (-x[0], -x[1], -x[2]))

        n = len(cuboids)
        dp = [0] * n
        
        # Iterate over all the boxes and for each box 
        # check if the previous box can sit on top of it
        for i in range(n):
           dp[i] = cuboids[i][2]
           for j in range(i):
            # If box j can stack on top of box i
            # we can add that height. We update the height such that we can maximize it
            if cuboids[j][0] <= cuboids[i][0] and \
                cuboids[j][1] <= cuboids[i][1] and \
                cuboids[j][2] <= cuboids[i][2] :
                # Update the height 
                dp[i] = max(dp[i], dp[j] + cuboids[i][2])
        return max(dp)
    
# Time complexity: O(N^2) as we iterate over the number of boxes twice. There is sorting overhead of NlogN but its less than N^2
# Space complexity: O(N) as we maintain a dp array of N boxes
    
maxHeight = Solution().maxHeight
print(maxHeight([[50,45,20],[95,37,53],[45,23,12], [50,50,50]]))
print(maxHeight([[50,45,20],[95,37,53],[45,23,12]]))
print(maxHeight([[38,25,45],[76,35,3]]))
print(maxHeight([[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]))