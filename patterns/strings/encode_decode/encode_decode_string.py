'''
LT 271: Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
'''
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        final_str = ''
        for s in strs:
            l = len(s)
            final_str += str(l) + 'LEN' + s
        return final_str
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        strs = []
        while s:
            l = int(s[0:s.index('LEN')])
            str_tmp = s[s.index('LEN')+3:s.index('LEN')+3+l]
            strs.append(str_tmp)
            s = s[s.index('LEN')+3+l:]
        return strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
