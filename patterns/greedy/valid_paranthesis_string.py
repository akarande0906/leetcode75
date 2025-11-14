'''
Leetcode 678: Valid Paranthesis String
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        # We maintain two stacks: For the brackets and for the stars
        bracket_stack, star_stack = [], []
        for i in range(len(s)):
            if s[i] == '(':
                bracket_stack.append(i)
            elif s[i] == ')':
                if bracket_stack:
                    bracket_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else: 
                    # We cannot eliminate the right bracket by either a left bracket
                    # or a star
                    return False
            else:
                star_stack.append(i)
        # Now we compare left over brackets and stars
        while bracket_stack and star_stack:
            if bracket_stack.pop() > star_stack.pop():
                # If the index of the element on the star stack is lesser than the element
                # on the bracket stack it means that this is invalid
                return False
        # Finally we return True only if there are no more elements in the bracket_stack
        return not bracket_stack

validBrack = Solution().checkValidString
print(validBrack("()"))
print(validBrack("(*)"))
print(validBrack("(*))"))
print(validBrack("((*)"))
print(validBrack("(((*)"))
print(validBrack("*****"))

# Time Complexity: O(n) as we iterate over the string once and then iterate over the stacks which can also be O(n)
# Space Complexity: O(n) for the two stacks

        
