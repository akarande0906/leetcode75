'''
LC 953: Verifying an Alien Dictionary
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.
Example 1: Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
'''
class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        for i in range(1, len(words)):
            min_len = min(len(words[i]),len(words[i-1]))
            if words[i][0:min_len] == words[i-1][0:min_len] and len(words[i]) < len(words[i-1]): 
                return False
            for j in range(min_len):
                if words[i][j] == words[i-1][j]:
                    continue
                elif order.find(words[i][j]) < order.find(words[i-1][j]):
                    return False
                else:
                    break
        return True   
    

''' Alternative Solution: Saves the overhead of the find operation
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for i, c in enumerate(order):
            order_map[c] = i
        for i in range(1, len(words)):
            min_len = min(len(words[i]),len(words[i-1]))
            if words[i][0:min_len] == words[i-1][0:min_len] and len(words[i]) < len(words[i-1]): 
                return False
            for j in range(min_len):
                if words[i][j] == words[i-1][j]:
                    continue
                elif order_map[words[i][j]] < order_map[words[i-1][j]]:
                    return False
                else:
                    break
        return True            
                
'''


is_srt = Solution().isAlienSorted
print (is_srt(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print (is_srt(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
print (is_srt(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))

                