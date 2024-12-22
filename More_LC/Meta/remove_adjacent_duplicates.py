'''
LC 1047: Remove All Adjacent Duplicates In String
You are given a string s consisting of lowercase English letters. 
A duplicate removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
Example 1: Input: s = "abbaca" Output: "ca"
Example 2: Input: s = "azxxzy" Output: "ay"
'''
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [s[0]]
        for i in range(1, len(s)):
            if stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)     

    # More concise 
    def removeDuplicates2(self, s: str)   -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack) 
        
remover = Solution().removeDuplicates2
print (remover('azxxzy'))
print (remover('abbaca'))
print (remover('abccba'))

'''
'''