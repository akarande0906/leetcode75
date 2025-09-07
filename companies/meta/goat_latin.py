'''
LC 824 Goat Latin
'''
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        arr = sentence.split(' ')
        for i in range(len(arr)):
            word = arr[i]
            if not word[0].lower() in vowel_set:
                if len(word) > 1:
                    word = word[1:] + word[0]
            word += 'ma' + 'a' * (i+1)
            arr[i] = word
        return ' '.join(arr)

                    
print (Solution().toGoatLatin('I speak Goat Latin'))
print (Solution().toGoatLatin('The quick brown fox jumped over the lazy dog'))