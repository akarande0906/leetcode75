'''
LC 2938: Separate White Balls and Black Balls
You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, 
respectively. In each step, you can choose two adjacent balls and swap them.
Return the minimum number of steps to group all the black balls to the right 
and all the white balls to the left.
'''
class Solution:
    def minimumSteps(self, s: str) -> int:
        # When ever we encounter a white ball, see how many black balls are preceeding it
        # For example 10101 : The first white ball will need 1 swap to become 01101 and the
        # Second white ball will need two swaps to go left
        swaps = 0
        black_balls = 0
        for c in s:
            if c == '0':
                swaps += black_balls
            else:
                black_balls += 1
        return swaps
    
# Time Complexity: O(N) where N is the number of elements in the string
# Space Complexity: O(1) as we are using only a constant space

print (Solution().minimumSteps("1100")) # 1
print (Solution().minimumSteps("110110")) # 2
print (Solution().minimumSteps("001111")) 
print (Solution().minimumSteps("10101")) 