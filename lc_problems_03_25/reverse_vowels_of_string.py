'''
LC 345: Reverse Vowels of a String
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','A','e','E','i', 'I', 'o', 'O', 'u', 'U'}
        left, right = 0, len(s) - 1
        str_arr = list(s)
        while left < right:
            if str_arr[left] in vowels and str_arr[right] in vowels:
                str_arr[left], str_arr[right] = str_arr[right], str_arr[left]
                left += 1
                right -= 1
            elif str_arr[left] in vowels:
                right -= 1
            elif str_arr[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1
        return ''.join(str_arr)
reverseVowels = Solution().reverseVowels
print(reverseVowels("hello"))
print(reverseVowels("leetcode"))
print(reverseVowels("aA"))
print(reverseVowels("IceCreAm"))
print(reverseVowels("racecar"))
print(reverseVowels("rythm"))
