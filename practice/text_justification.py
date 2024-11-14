'''
Leet code: 68 (Hard: O(n) where n is the total number of chars
'''
class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        cur_len = 0
        output_array = []
        cur_arr = []
        for word in words:
            if cur_len + len(word) +len(cur_arr) > maxWidth:
                spaces = maxWidth - cur_len
                # Count number of spaces to add
                if len(cur_arr) == 1:
                    output_array.append(cur_arr[0] + ' ' * spaces)
                else:
                    spaces = spaces // (len(cur_arr) - 1)
                    extra_spaces = (maxWidth - cur_len) % (len(cur_arr) - 1)
                    val = ''
                    for i in range(len(cur_arr) - 1):
                        val += cur_arr[i] + ' ' * (spaces + (i < extra_spaces))
                    spaces = maxWidth - len(val) - len(cur_arr[-1])
                    val += ' ' * spaces + cur_arr[-1]
                    output_array.append(val)
                cur_arr.clear()
                cur_len = 0
            
            cur_arr.append(word)
            cur_len += len(word)
        if cur_arr:
            val = ' '.join(cur_arr)
            val += ' ' * (maxWidth - len(val))
            output_array.append(val)
        return output_array

justify = Solution().fullJustify
print(justify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(justify(["What","must","be","acknowledgment","shall","be"], 16))
print(justify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))
            
