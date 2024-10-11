'''
Reverse the order of words in a given sentence (a string of words).
'''

def reverse_words(sentence):
    arr = sentence.split(' ')
    str = ' '.join(arr[::-1])
    return str

if __name__ == '__main__':
    str = 'Hello how are you'
    print (reverse_words(str))
