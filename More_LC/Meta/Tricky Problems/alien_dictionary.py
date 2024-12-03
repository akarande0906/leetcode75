'''
LC 269: Alien Dictionary
There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.
You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are
sorted lexicographically by the rules of this new language.
Example: Input: words = ["wrt","wrf","er","ett","rftt"] Output: "wertf"
Input: words = ["z","x","z"] Output: "" Explanation: The order is invalid, so return "".
'''
class Solution:
    def alienOrder(self, words: list[str]) -> str:
        adj = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minlen = min(len(w1), len(w2))
            # If both strings have same prefix but longer string is earlier 
            # in the order, this is invalid
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen): # Only need to compare the length of the smaller word
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = {} # If False it means visited but not in current path
                    # If True means visited and in current path
        result = []

        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True # Include in current path
            for nbr in adj[c]:
                # If it returns true it means this was visited
                # twice in the current path and therefore is a loop
                if dfs(nbr):
                    return True
            visit[c] = False # Remove from the current path
            # Post order traversal. Add at the end. This is done
            # To ensure lexigraphical sorting. For example:
            # A -> B -> C
            # '---------'
            result.append(c) 
                
        for c in adj:
            if dfs(c): 
                return "" # If we get a true, it means there was a loop
        # Since we are doing post order it will add in reverse
        result.reverse()
        return ''.join(result)

alien = Solution().alienOrder
print(alien(["wrt","wrf","er","ett","rftt"]))
print(alien(["z","x"]))
print(alien(["z","x", "z"]))

