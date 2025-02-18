'''
LC 1209: Remove All Adjacent Duplicates in String II
'''
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        cur_count = 1
        cur_char = s[0]
        
        def check_stack(cur_char, cur_count, new_char):
            if cur_count >= k:
                # Remove the num of chars after 
                # dividing by k
                cur_count = cur_count % k 
            if stack and stack[-1][0] == cur_char:
                cur_count = (cur_count + len(stack[-1])) % k
                stack.pop()
            if cur_count:
                stack.append(cur_char * cur_count)
            
        for id in range(1, len(s)):
            if cur_char != s[id]:
                check_stack(cur_char, cur_count, s[id])
                cur_char = s[id]
                cur_count = 1
            else:
                cur_count += 1
        if cur_count:
            check_stack(cur_char, cur_count, '')
        return ''.join(stack)

# Time: O(n)
# Space: O(n)
removeDuplicates = Solution().removeDuplicates
print (removeDuplicates("abcd", 2))
print (removeDuplicates("deeedbbcccbdaa", 3))
print (removeDuplicates("pbbcggttciiippooaais", 2))
print (removeDuplicates("aabccddb", 2))