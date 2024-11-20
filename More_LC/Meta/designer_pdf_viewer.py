#!/bin/python3
'''
When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. 
In this PDF viewer, each word is highlighted independently. For example:
Example
 
The heights are  [1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5] and abc. 
The tallest letter is  3 high and there are 3 letters. 
Therefore highlighted area is  9 mm^2
'''

import math
import os
import random
import re
import sys

def designerPdfViewer(h, word):
    # Write your code here
    max_ht = 0
    for c in word:
        ht = h[ord(c) - ord('a')]
        max_ht = max(ht, max_ht)
    return max_ht * len(word)

if __name__ == '__main__':
    heights = ['1', '3', '1', '3', '1', '4', '1', '3', '2', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5']
    word = 'torn'
    print (designerPdfViewer(list(map(int,heights)), word))