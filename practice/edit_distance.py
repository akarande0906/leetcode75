'''
Leetcode: 72 (Hard, Complexity: O(m*n) where m is length of word1 and n is length of word2
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        Initialize 2 D array for word1 and word2 with the base case of 
        having an empty string to word1 and empty string to word2
        E.g. Word1 = kart Word2 = arc => remove k and replace t with c: 2 steps
            ""  k   a   r   t 
        ""  0   1   2   3   4
        a   1   1   1   2   3
        r   2   2   2   1   2
        c   3   3   3   2   2

        When we add a character we increment word2 pointer since 
        we assume we inserted a char from word 2.
        When we delete a character we increment word1 pointer.
        if we replace a character then we have to increment both word1
        and word2 pointers
        '''
        dp = [[ 0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
        # Initialize the dp array for empty string conversions
        for i in range(len(word1) + 1):
            dp[0][i] = i
        for j in range(len(word2) + 1):
            dp[j][0] = j
        print (dp)
        for j in range(1, len(word2) + 1):
            for i in range(1, len(word1) + 1):
                if word1[i-1] == word2[j-1]:
                    # We compare the prev indices as 0, 0 are used for 
                    # empty string comparison
                    dp[j][i] = dp[j-1][i-1]
                else:
                    dp[j][i] =  1 + min(dp[j][i-1], dp[j-1][i], dp[j-1][i-1])
        return dp[j][i]        

print (Solution().minDistance('kart', 'arc'))
print (Solution().minDistance('horse', 'ros'))
print (Solution().minDistance('horse', 'roc'))

