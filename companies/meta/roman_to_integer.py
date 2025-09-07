'''
LC: 13. Roman to Integer
Given a roman numeral, convert it to an integer.
'''
mapper = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000, 
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

class Solution:

    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in mapper:
                total += mapper[s[i:i+2]]
                i += 2
            else:
                total += mapper[s[i]]
                i += 1
        return total
    
# Time Complexity: O(N) where N is the length of the string
# Space Complexity: O(1) as we only store constant values in the map and no extra space is used

rtoi = Solution().romanToInt
print(rtoi('MMMDCCXLIX'))
print(rtoi('LVIII'))
print(rtoi('MCMXCIV'))
print(rtoi('MMMCMXCVIII'))
