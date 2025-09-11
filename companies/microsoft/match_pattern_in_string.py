'''
Leetcode 3407: Substring Match Pattern
'''
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        # find the index of the * char
        star_id = p.find('*')
        if star_id != -1:
            left_str = p[:star_id]
            right_str = p[star_id+1:]
            left_find = s.find(left_str)
            if left_find != -1:
                right_find = s[left_find + len(left_str):].find(right_str)
                if right_find != -1:
                    return True
        return False

match = Solution().hasMatch
print(match('leetcode', 'ee*e'))
print(match('car', 'c*v'))
print(match('luck', 'u*'))
print(match('luck', '*'))
