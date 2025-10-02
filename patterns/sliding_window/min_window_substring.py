'''
Leetcode 76: Minimum Window Substring
'''
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""
        
        window = defaultdict(int)
        count_t = Counter(t)
        # need is the char count we want
        have, need = 0, len(count_t)
        result, result_length = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            # We only need to do this if the counts match
            # we dont have to do this for a repeated instance of a char
            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            # Once we have a match, we do this to update the window to find other substrings
            # The while ensures we remove all characters that are not in t
            while have == need:
                # If the new length is shorter we update the result length
                if (r - l + 1) < result_length:
                    result = [l, r]
                    result_length = r - l + 1
                # Remove the left most character from the window 
                window[s[l]] -= 1
                # Check if the character being removed is present in t 
                # and if removal reduces count to less than what is needed
                # in which case we have to reduce our have count
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = result
        return s[l : r+1] if result_length != float('inf') else ""
    

min_win = Solution().minWindow
print(min_win('OUZODYXAZV', 'XYZ'))
print(min_win('xyz', 'xyz'))
print(min_win('x', 'xy'))
print(min_win('ADOBECODEBANC', 'ABC'))

# Time Complexity: O(n + m) where n = len(s) and m = len(m)
# Space Complexity: O(m) as we maintain a map to hold the counts



                


