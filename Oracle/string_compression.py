'''
LC 443: String Compression
'''
class Solution:

    def compress(self, chars: list[str]) -> int:
        cur_id = 0
        cur_char = chars[0]
        cur_count = 1
        char_len = len(chars)

        def update_encoded_string(cur_char, group_count):
            nonlocal cur_id
            chars[cur_id] = cur_char
            cur_id += 1
            temp_arr = []
            if group_count != 1:
                str_repr = str(group_count)
                chars[cur_id:cur_id+len(str_repr)] = list(str_repr)
                cur_id += len(str_repr)


        for i in range(1, char_len):
            if cur_char != chars[i]:
                update_encoded_string(cur_char, cur_count)
                cur_char = chars[i]
                cur_count = 1
            else:
                cur_count += 1
        if cur_char:
            update_encoded_string(cur_char, cur_count)
        print (chars[:cur_id])
        return cur_id
                    
# Time: O(n)
# Space: O(1)
compress = Solution().compress
print (compress(["a","a","b","b","c","c","c"]))
print (compress(["a"]))
print (compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
print (compress(["a","a","a","b","b","a","a"]))
print (compress(["a","a","a","b","b","c","c","c"]))




                    

