'''
LC: 91
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        Can use DP?
        Go character by character
        11106:
        1 -> A and 1106, then 1 -> A and 106 or 11 -> K and 06
        But 06 is not valid, so terminate this.
        Therefore AAJF or KJF
        '''
        memo = {}
        def recursiveWithMemo(index, s):
            if index in memo:
                return memo[index]
            if index == len(s):
                return 1 # End of string
            if s[index] == '0':
                return 0
            if index == len(s) - 1:
                return 1 # Single digit is valid
            answer = recursiveWithMemo(index + 1, s)
            if int(s[index: index + 2]) <=26: # If 2 chars represent an alphabet
                answer += recursiveWithMemo(index + 2, s)
            memo[index] = answer
            return answer
        return recursiveWithMemo(0, s)a


        ''' Tabulation 
        def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1 # Base case
        dp[1] = 0 if s[0] == '0' else 1
        for i in range (2, len(s)+1):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            two_digit = int(s[i-2:i])
            if two_digit >= 10 and two_digit <=26:
                dp[i] += dp[i-2]
        return dp[len(s)]
        '''

        '''
        Tabulation with 0(1) space
        def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0
        prev_two = 1
        prev_one = 1
        for i in range (1, len(s)):
            current = 0
            if s[i] != '0':
                current = prev_one
            two_digit = int(s[i-1:i+1])
            if two_digit >= 10 and two_digit <=26:
                current += prev_two
            prev_two = prev_one
            prev_one = current
        return prev_one
        '''


