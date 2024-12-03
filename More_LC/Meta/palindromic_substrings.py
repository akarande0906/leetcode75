'''
LC 647: Palindromic Substrings
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.
Example: Input: s = "abc" Output: 3 Explanation: Three palindromic strings: "a", "b", "c".
Input: s = "aaa" Output: 6 Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        self.target_array = []
        ans = 0
        for i in range(len(s)):
            ans += self.countPalindromesAroundCenter(s, i, i) # Odd length palindromes
            ans += self.countPalindromesAroundCenter(s, i, i+1) # Even length palindromes
        print (self.target_array)
        return ans

    def countPalindromesAroundCenter(self, s, start, end):
        ans = 0
        while start >= 0 and end < len(s):
            if s[start] != s[end]:
                break
            self.target_array.append(s[start:end+1])
            start -= 1
            end += 1
            ans += 1
        return ans

countPals = Solution().countSubstrings
print (countPals('aaa'))
print (countPals('abc'))
print (countPals('madam'))