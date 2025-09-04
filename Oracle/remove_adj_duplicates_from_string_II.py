'''
LC 1209: Remove All Adjacent Duplicates in String II
'''
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['$', 0]] # Dummy init value
        
        for char in s:
            if stack[-1][0] == char: # repeated
                stack[-1][1] += 1 # Increment count
                if stack[-1][1] == k:
                    stack.pop() # We've reached the dup count. Pop
            else:
                stack.append([char, 1]) # New character. Can add to stack
            
        # Finally read stack from left to right and generate string
        # The dummy entry will not be included because of the 0
        return ''.join(c * count for c, count in stack) 



# Time: O(n)
# Space: O(n)
removeDuplicates = Solution().removeDuplicates
print (removeDuplicates("abcd", 2))
print (removeDuplicates("deeedbbcccbdaa", 3))
print (removeDuplicates("pbbcggttciiippooaais", 2))
print (removeDuplicates("aabccddb", 2))