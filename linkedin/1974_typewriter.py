class Solution:
    def minTimeToType(self, word: str) -> int:
        prevChar = 'a'
        totalSeconds = 0
        for char in word:
            if ord(prevChar) == ord(char):
                totalSeconds += 1
            else:
                # Compute the time taken to move from prevChar to new char
                rotationTime = abs(ord(char) - ord(prevChar))
                #rotationTime = rotationTime % 26
                if rotationTime > 13:
                    rotationTime = 26 - rotationTime
                totalSeconds += rotationTime + 1
            prevChar = char
        return totalSeconds

print(Solution().minTimeToType('abc'))
print(Solution().minTimeToType('bza'))
print(Solution().minTimeToType('azbycx'))
