class Solution:
    def myAtoi(self, s: str) -> int:
        neg = False
        visited = set()
        lastchr = ''
        retVal = ''
        for c in s:
            if c == ' ':
                if lastchr == ' ' or not lastchr:
                    continue
                else:
                    break
            elif c == '-' or c == '+':
                if lastchr == '-' or lastchr == '+':
                    break
                elif lastchr == ' ' or not lastchr:
                    if c == '-':
                        neg = True
                    lastchr = c
                    continue
                elif lastchr >= '0' or lastchr <= '9':
                    break
            elif c == '0':
                if lastchr >= '0' or lastchr <= '9': 
                    retVal += c
                lastchr = c
                continue
            elif c >= '1' and c <= '9':
                retVal += c
                lastchr = c
            else:
                break
        if retVal:
            val = int(retVal)
            if neg:
                val = -(val)
            if val < -2 ** 31:
                val = -2 ** 31
            elif val > 2 ** 31 - 1:
                val = 2 ** 31 - 1
            return val
        else:
            return 0


print(Solution().myAtoi('words and 987'))
print(Solution().myAtoi('0-1'))
print(Solution().myAtoi('1337c0d3'))
print(Solution().myAtoi('   -042'))
print(Solution().myAtoi('42'))
