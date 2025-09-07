'''
LC 161: Given two strings, check what it will take to transform one word to the other in exactly one edit.
Each edit is by:
- Adding one character
- Removing one character
- Converting one character

Example: cat and dog => False, cat and cast => True, bat and bot => True
'''

def one_edit_apart(word1, word2):
    if len(word1) > len(word2):
        word1, word2 = word2, word1
    edits = 0
    j = 0
    if not word1 and not word2:
        return True
    elif not word1 or not word2:
        return False
    elif len(word2) - len(word1) > 1:
        return False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            # Then check if lenghts are the same, we can try to convert
            if len(word1) == len(word2):
                return word1[i+1:] == word2[i+1:]
            else:
                return word1[i:] == word2[i+1:]
    # Finally only condition left if the last character of word2 is different
    return len(word1) + 1 == len(word2)


print (one_edit_apart('cat', 'catho'))
print (one_edit_apart('cat', 'dog'))
print (one_edit_apart('cat', 'cast'))
print (one_edit_apart('cat', 'cut'))
print (one_edit_apart('cat', 'act'))
print (one_edit_apart('cat', ''))
print (one_edit_apart('cat', 'at'))