'''
LC 75: Simplify Unix Path
Example: /home/ to /home
/home//foo/  to /home/foo
/home/user/Documents/../Pictures to /home/user/Pictures
/../ to / -> Cannot go up one level from root
/.../a/../b/c/../d/./ to /.../b/d  -> ... is a valid directory name
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for char in path.split('/'):
            if char == '..':
                if stack: # Go up one directory
                    stack.pop()
            elif char == '.' or not char: # Current directory or empty space
                continue
            else:
                stack.append(char)
        return '/' + '/'.join(stack)
    
simplify = Solution().simplifyPath
print (simplify('/home/'))
print (simplify('/home/user/Documents/../Picture/'))
print (simplify('/.../a/../b/c/../d/./'))
print (simplify('/..'))
