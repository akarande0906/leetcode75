'''
Reverse the order of words in a given sentence (a string of words).
'''

def reverse_words(sentence):
    arr = sentence.split(' ')
    str = ' '.join(arr[::-1])
    return str

def rev_words_2(sentence):
    arr  = sentence.split(' ')
    str = ''
    for pos in range(len(arr) - 1, -1, -1):
        str += arr[pos] + ' '
    return str.strip()


if __name__ == '__main__':
    str = 'Hello how are you'
    print (reverse_words(str))
    print (rev_words_2(str))
