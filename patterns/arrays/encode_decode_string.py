'''
Leetcode 271: Encode and Decode Strings
'''
from typing import List


class Codec:
    # We create the string in the format : <len_of_str1>#<str1><len_of_str2>#<str2>.....
    def encode(self, strs: List[str]) -> str:
        final_str = ''
        for s in strs:
            final_str += str(len(s)) + '#' + s
        return final_str
    
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        #print (s)
        while s:
            hash_index = s.index('#')
            length = int(s[0:hash_index])
            #print (s[hash_index + 1 : hash_index + 1 + length])
            decoded_strs.append(s[hash_index + 1 : hash_index + 1 + length])
            s = s[hash_index + 1 + length:]
        return decoded_strs
    

codec = Codec()
array = ["Hello","World"]
assert array == codec.decode(codec.encode(array))
array = ["This", "#is#", "no", "joke"]
assert array == codec.decode(codec.encode(array))

