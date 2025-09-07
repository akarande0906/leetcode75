'''
LC 424: Longest Repeating Character Replacement
Return the length of the longest substring containing the same letter 
you can get after performing the above operations.
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Use sliding window
        n = len(s)
        # Iterate over all chars from A to Z
        '''
        for c in range (ord('A'), ord('Z') + 1):
            c = chr(c)
            i, j, r = 0, 0, 0
            while j < n:
                if s[j] == c:
                    j+= 1 
                elif r < k:
                    j += 1
                    r += 1
                elif s[i] == c:
                    i+= 1
                else:
                    i += 1
                    r -= 1
                ans = max(ans, j - i)
        return ans
        '''
        count = {}
        l, r = 0, 0
        res = 0
        for r in range(n):
            count[s[r]] = count.get(s[r], 0) + 1
            if (r - l + 1) - max(count.values()) <= k: # This will be an O(26) operation
                res = max(res, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1

        return res
    
    def characterReplacement2(self, s: str, k: int) -> int:
        count = {}
        l, r = 0, 0
        n = len(s) 
        max_freq = 0
        res = 0
        for r in range(n):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])
            if (r - l + 1) - max_freq <= k:
                res = max(res, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1

        return res

print (Solution().characterReplacement2("AAABCACB", 2)) # 4
print (Solution().characterReplacement2("ABAB", 2)) # 4
print (Solution().characterReplacement2("AABABBA", 1)) # 4
print (Solution().characterReplacement2("AABABBA", 2)) # 5

# Time Complexity: O(N) where N is the number of elements in the string
# Space Complexity: O(26) as we are using a dictionary of 26 elements
# The second solution is a bit more optimized as we are not calculating the max of the dictionary values each time