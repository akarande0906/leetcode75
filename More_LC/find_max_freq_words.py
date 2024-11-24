'''
Given a list of sentences find the k words with max frequency
'''
import heapq
from collections import Counter

def getMaxWords(k, words):
    # k is the number of freq words to return
    # words is an array of sentences
    # Time Complexity : O(nlogn)
    word_list = [sentence.split() for sentence in words]
    counter = Counter(word for words in word_list for word in words)
    print (counter)
    cnt = 0
    return_arr = []
    for key,val in counter.most_common():
        cnt += 1
        return_arr.append(key)
        if cnt >= k:
            return return_arr



print(getMaxWords(3, ['gfg is best for geeks', 'geeks love gfg', 'gfg is best']))
