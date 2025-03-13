'''
LC 2375: Smallest Number from DI String
'''
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        '''
        Add each index + 1 to a stack
        If the char at index is I pop from the stack and add to O/P
        If the char at index is D keep the element on stack
        Finally at the end pop out all the remaining elems and add to O/P
        ''' 
        stack, output = [], []
        for idx in range (len(pattern) + 1):
            stack.append(idx+1)
            while stack and (idx == len(pattern) or pattern[idx] == 'I'):
                output.append(str(stack.pop()))
        return ''.join(output)
    
    # Alternative approach: More intuitive??
    def smallestNumber_v2(self, pattern: str) -> str:
        '''
        Add each index + 1 to a stack
        If the char at index is I pop from the stack and add to O/P
        If the char at index is D keep the element on stack
        Finally at the end pop out all the remaining elems and add to O/P
        ''' 
        stack, output = [], []
        n = len(pattern)
        for idx in range (n):
            stack.append(idx+1)
            while stack and pattern[idx] == 'I':
                output.append(str(stack.pop()))
        stack.append(n+1)
        while stack:
            output.append(str(stack.pop()))
        return ''.join(output)


# Time Complextiy : O(n)
# Space Complexity : O(n)
smallestNumber = Solution().smallestNumber
print(smallestNumber("IDID"))
print(smallestNumber("III"))
print(smallestNumber("IIIDIDDD"))
print(smallestNumber("DIDI"))
