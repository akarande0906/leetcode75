'''
LeetCode: 408: Valid Word Abbreviation
'''
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        cur_num = -1
        j = 0
        for i in range(len(abbr)):
            if abbr[i] >= '0' and abbr[i] <= '9':
                if cur_num == -1:
                    cur_num = int(abbr[i])
                    if cur_num == 0:
                        return False
                else:
                    cur_num = cur_num * 10 + int(abbr[i])
            else:
                if cur_num != -1:
                    if j + cur_num > len(word):
                        return False
                    else:
                        j += cur_num
                        cur_num = -1
                if j >= len(word) or abbr[i] != word[j]:
                    return False
                j += 1
        if cur_num != -1:
            return True if cur_num + j == len(word) else False
        else:
            return True if j == len(word) else False
        return True

validAbbr = Solution().validWordAbbreviation
print(validAbbr('internationalization', 'i12iz4n'))
print(validAbbr('apple', 'a2e'))
print(validAbbr('substitution', '12'))
print(validAbbr('internationalization', 'i5a11o1'))
