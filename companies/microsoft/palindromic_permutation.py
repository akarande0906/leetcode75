'''
Check if a String can have a permutation thats a palindrome
For example: Madamadamiam can be rearranged to 'Madam I am Adam' 
'''
from collections import Counter

class Solution():
    def isPalindromicPermutation(self, s: str) -> bool:
        # To find if a string is a palindrome, we should have all character counts as even except at most one
        # For example: abba is a palindrome and so is abcba, aabbcc can be rearranged to a palindrome, so can aabbc
        # To check we use a counter go count all the characters, then iter over the map to check if there are more than
        # one count thats odd
        s = s.lower()
        s.replace(' ', '')
        c = Counter(s)
        oddCount = 0
        for v in c.values():
            if v % 2:
                oddCount += 1
                if oddCount > 1:
                    return False
        return True
    
palin = Solution().isPalindromicPermutation
print(palin('aabbcc'))
print(palin('aabcc'))
print(palin('abcabcd'))
print(palin('geeksforgeeks'))
print(palin('geeksogeeks'))
print(palin('Hello there'))

# Time Complexity: O(n) as we construct a counter and then iterate over it
# Space Complexity: O(n) to build the counter, in the worst case each character appears once