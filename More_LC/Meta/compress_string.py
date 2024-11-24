'''
Given an array: [a,a,a,b,b,c,c,c] => return string 'a3b2c3' 
if [a] return [a] 
Repeat with in place update of array : [a,3,b,2,c,3]
'''

class Solution:
    def getCompressedString(self, array):
        if not array:
            return ''
        elif len(array) == 1:
            return array[0]
        prev_char = array[0]
        cur_len = 1
        final_str = ''
        for id in range(1, len(array)):
            if array[id] == array[id - 1]:
                cur_len += 1
            else:
                final_str += prev_char + str(cur_len)
                cur_len = 1
                prev_char = array[id]
        final_str += prev_char + str(cur_len)  
        return final_str
    
    def getCompressedStringRep(self, array):
        if not array:
            return ''
        elif len(array) == 1:
            return array[0]
        prev_char = array[0]
        cur_len = 1
        offset = 0
        for id in range(1, len(array)):
            if array[id] == prev_char:
                cur_len += 1
            else:
                array[offset] = prev_char
                prev_char = array[id]
                if cur_len > 1:
                    offset += 1
                    array[offset] = str(cur_len)
                offset += 1
                cur_len = 1
        array[offset] = prev_char
        if cur_len > 1:
            array[offset + 1] = str(cur_len) 
        offset += 2
        while offset < len(array):
            array[offset] = ''
            offset += 1
        return array

print (Solution().getCompressedStringRep(['a', 'a', 'b', 'b', 'c', 'c', 'c'])) 
print (Solution().getCompressedStringRep(['a', 'b', 'b', 'b', 'b', 'b', 'b']))
print (Solution().getCompressedStringRep(['a', 'b', 'c', 'd', 'e', 'f', 'g'])) 