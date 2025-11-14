'''
Leetcode 127: Word Ladder
'''
from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        # We create a graph of patterns such that we find adjacent 
        # nodes for each letter that separates by one character
        # For example: hot can be *ot, h*t or ho* and we find words that match 
        # one of these patterns and then navigate to these words as neighbors.

        adj_list = defaultdict(list)
        wordSet = set(wordList)
        wordSet.add(beginWord)
        # Generate the Adj list
        for word in wordSet:
            for p in range(len(word)):
                # Replace pth letter by * to generate pattern
                pattern = word[:p] + '*' + word[p+1:]
                adj_list[pattern].append(word)
        
        # Lets use BFS to run through the adj list and find the shortest path
        path_len = 1 # As we assume begin word is part of the path
        visited = set()
        queue = deque([beginWord])
        visited.add(beginWord)
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return path_len                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                # Lets find neighbors based on the pattern
                for p in range(len(word)):
                    # Replace pth letter by * to generate pattern
                    pattern = word[:p] + '*' + word[p+1:]
                    neighbors = adj_list[pattern]
                    for nbr in neighbors: 
                        if not nbr in visited:
                            queue.append(nbr)
                            visited.add(nbr)
            path_len += 1
        # No match found
        return 0
    
# Time Complexity: O(n*m*m) since we iterate over n words with length m, and we iterate over m chars to generate the pattern
# Space Complexity: O(n*m*m) since we update the queue with at max n words of m chars and m patterns

ladder = Solution().ladderLength
print(ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(ladder("hit", "cog", ["hot","dot","dog","lot","log"]))
        