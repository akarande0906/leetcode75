'''
LC 38: Count and Say
Run-length encoding is a fast and simple method of encoding strings.
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        def findRLE(val):
            temp_arr = []
            if val == '1':
                return '11'
            cur_char = val[0]
            cur_count = 1
            for i in range (1, len(val)):
                if val[i] == val[i-1]:
                    cur_count += 1
                else:
                    temp_arr.append(str(cur_count))
                    temp_arr.append(str(cur_char))
                    cur_count = 1
                    cur_char = val[i]
            # Now we handle the last char in case we have cur_count
            temp_arr.append(str(cur_count))
            temp_arr.append(str(cur_char))
            return ''.join(temp_arr)
        
        if n == 1:
            return '1'
        encoded_str = '1'
        for i in range(2, n+1):
            encoded_str= findRLE(encoded_str)
        return encoded_str
# TC: O(N * 2^N) where N is the number of elements in the string
# SC: O(N) where N is the number of elements in the string
finder = Solution().countAndSay
print (finder(1)) # 1
print (finder(4)) # 1211
print (finder(5)) # 111221