'''
LC 1216: Valid Palindrome III : Given a string s and an integer k, return true if s is a k-palindrome.
A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.
Example: Input: s = "abcdeca", k = 2 Output: true
Explanation: Remove 'b' and 'e' characters.
'''
from collections import deque
from functools import cache
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        queue = deque()
        queue.append((0, len(s) - 1, 0))
        visited = [[False for _ in range(len(s))] for _ in range(len(s))]
        while queue:
            left, right, cur_k = queue.popleft()
            if cur_k > k :
                return False
            while s[left] == s[right]:
                left += 1
                right -= 1
                if left >= right:
                    return True
            if not visited[left+1][right]:
                queue.append((left+1, right, cur_k+1))
                visited[left+1][right] = True
            if not visited[left][right-1]:
                queue.append((left, right-1, cur_k+1))
                visited[left][right-1] = True
        return True

    def isValidPalindromeIII(self, s:str, k:int) -> bool:
        visited = [[False for _ in range(len(s))] for _ in range(len(s))]
        @cache
        def isPalindrome(s, lptr, rptr, changes):
            if changes > k:
                return False
            if rptr - lptr + 1 <=0:
                return True
            while lptr <= rptr:
                if s[lptr] == s[rptr]:
                    lptr += 1
                    rptr -= 1
                    if lptr > rptr:
                        return True
                else:
                    break
            if not visited[lptr+1][rptr]:
                visited[lptr+1][rptr] =  isPalindrome(s, lptr+1, rptr, changes+1)  
            if not visited[lptr][rptr-1]:
                visited[lptr][rptr-1] = isPalindrome(s, lptr, rptr-1, changes+1)
            return visited[lptr+1][rptr] or visited[lptr][rptr-1]
                