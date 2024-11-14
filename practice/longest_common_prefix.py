class Solution:
    def longestCommonPrefix(self, word_list):
        if not word_list:
            return ''
        n = len(word_list)
        min_len_string = float('inf')
        for str in word_list:
            if len(str) < min_len_string:
                min_len_string = len(str)
        i = 0
        while i < min_len_string:
            for str in word_list:
                if str[i] != word_list[0][i]:
                    return str[:i]
            i += 1
        return str[0][:i]


print (Solution().longestCommonPrefix(['flower', 'flow', 'florida', 'floatsam']))
print (Solution().longestCommonPrefix(['absolute', 'absent', 'absel']))

