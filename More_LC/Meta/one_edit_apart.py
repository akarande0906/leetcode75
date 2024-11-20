'''
Given two strings, check what it will take to transform one word to the other in exactly one edit.
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
    for i in range(len(word1)):
        if word1[i] == word2[j]:
            j += 1
        else:
            if len(word1) == len(word2): # increment edits and advance the pointer
                j += 1
                edits += 1
                if edits > 1:
                    return False
    return True

print (one_edit_apart('cat', 'dog'))
print (one_edit_apart('cat', 'cast'))
print (one_edit_apart('cat', 'cut'))
print (one_edit_apart('cat', 'act'))
print (one_edit_apart('cat', ''))
print (one_edit_apart('cat', 'at'))