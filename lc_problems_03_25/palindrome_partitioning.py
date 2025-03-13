'''
LC 131: Palindrome Partitioning
'''
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        str_len = len(s)
        dp = {}
        result = []

        def isPalindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def iterate(index, temp_list):
            if index == str_len:
                result.append(temp_list[:])
                return
            for i in range(index, str_len):
                if not (index, i) in dp:
                    dp[(index, i)] = isPalindrome(index, i)
                if dp[(index, i)]:
                    temp_list.append(s[index : i+1])
                    iterate(i+1, temp_list)
                    temp_list.pop()
        
        iterate(0, [])
        return result   

# Time Complexity: O(n * 2^n)     
# Space complexity: O(n * n) considering the stack space and the dp map

partition = Solution().partition
print(partition("aab"))
print(partition("a"))
print(partition("aabb"))