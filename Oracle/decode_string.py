'''
LC 394: Decode String
'''
# When we see an opening [ we push  the previous number and string on the stack
# When we see a closing ] we fetch the previous string and number from the stack and 
class Solution:
    def decodeString(self, s: str) -> str:
        cur_num = 0
        cur_str = ''
        stack = []
        num = 0
        temp_str = ''
        for c in s:
            if c >= '0' and c <= '9':
                num = num * 10 + int(c)
            elif c == '[':
                stack.append((temp_str, num))
                num = 0
                temp_str = ''
            elif c == ']':
                strng, n = stack.pop()
                temp_str = strng + temp_str * n
            else:
                temp_str += c
        return temp_str
                      



# Time: O(n)
# Space: O(n)
decodeString = Solution().decodeString
print (decodeString("3[a]2[bc]"))
print (decodeString("3[a2[c]]"))
print (decodeString("2[abc]3[cd]ef"))