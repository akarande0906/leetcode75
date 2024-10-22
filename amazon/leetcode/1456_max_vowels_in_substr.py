class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vset = {'a','e', 'i', 'o', 'u'}
        lptr = 0
        maxlen = 0
        curlen = 0
        tempstr = ''
        if not s:
            return 0
        for rptr in range(0, len(s)): 
            if s[rptr] in vset:
                curlen += 1
            if rptr - lptr == k - 1:
                maxlen = max(maxlen, curlen)
                #tempstr = s[lptr:rptr+1]
                if s[lptr] in vset:
                    curlen -= 1
                lptr+= 1
        return maxlen

print(Solution().maxVowels("abciiidef", 3))
print(Solution().maxVowels("aeiou", 2))
print(Solution().maxVowels("leetcode", 3))
