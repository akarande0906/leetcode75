class Solution:
    def optimalPartition(self, input: str) -> int:
        seen = set()
        substr_count = 1 # This is done because we increment the count only if there is a duplicate char
        for char in input:
            if char in seen:
                substr_count += 1
                seen.clear()
            seen.add(char)
        return substr_count

print(Solution().optimalPartition('abacaba'))
print(Solution().optimalPartition('abcdefghijkl'))
print(Solution().optimalPartition('aaaaa'))
