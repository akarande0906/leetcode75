'''
LC 205: 
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # When we map a char we check if its there already
        s_t_map = {}
        t_s_map = {}

        for i in range(len(s)):
            if s[i] in s_t_map and s_t_map[s[i]] != t[i]:
                return False
            elif s[i] not in s_t_map:
                s_t_map[s[i]] = t[i]
            if t[i] in t_s_map and t_s_map[t[i]] != s[i]:
                return False
            elif t[i] not in t_s_map:
                t_s_map[t[i]] = s[i]
        return True
    
# TC : O(n)
# SC : O(n)

isIsomorphic = Solution().isIsomorphic
print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("badc", "baba"))
print(isIsomorphic("ab", "aa"))