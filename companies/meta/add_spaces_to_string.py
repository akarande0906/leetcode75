'''
LC 2109: Adding Spaces to String
You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. 
Each space should be inserted before the character at the given index.
For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. 
Thus, we obtain "Enjoy Your Coffee". Return the modified string after the spaces have been added.
Example: Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15] Output: "Leetcode Helps Me Learn"
'''
class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        n = len(s) - 1
        cur_offset = 0
        ret_str = ''
        for space in spaces:
            #if space == 0:
            #    ret_str = ' '
            space, cur_offset = space - cur_offset, space
            ret_str += s[:space] + ' '
            s = s[space:]
        if s:
            ret_str += s
        return ret_str
    
    ''' More efficient : 2 pointer'''
    def addSpaces2Ptr(self, s: str, spaces: list[int]) -> str:
        n = len(s) - 1
        cur_offset = 0
        ret_arr = []
        for space in spaces:
            ret_arr.append(s[cur_offset:space])
            cur_offset = space
        if cur_offset < len(s):
            ret_arr.append(s[cur_offset:])
        return ' '.join(ret_arr)

#spacer = Solution().addSpaces
spacer = Solution().addSpaces2Ptr
print (spacer("spacing", [0,1,2,3,4,5,6]))
print (spacer("icodeinpython", [1,5,7,9]))
print (spacer("LeetcodeHelpsMeLearn", [8,13,15]))
            
        