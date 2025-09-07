class TrieNode:
    def __init__(self, text = ''):
        self.children = {}
        self.text = text
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        if not word:
            return
        cur = self.root
        for i, c in enumerate(word):
            if not c in cur.children:
                prefix = word[0: i+1]
                cur.children[c] = TrieNode(prefix)
            cur = cur.children[c]
        cur.is_word = True
    
    def search(self, word):
        if not word:
            return False
        cur = self.root
        for c in word:
            if not c in cur.children:
                return False
            cur = cur.children[c]
        return cur.is_word
    
    def _find_child_word(self, node, words):
        if node and node.is_word:
            words.append(node.text)
        for c in node.children:
            self._find_child_word(node.children[c], words)
    
    def find_child_words(self, prefix):
        words = []
        if not prefix:
            return False
        cur = self.root
        for c in prefix:
            if not c in cur.children:
                return []
            cur = cur.children[c]
        self._find_child_word(cur, words)
        return words

    
    def starts_with(self, prefix):
        if not prefix:
            return False
        cur = self.root
        for c in prefix:
            if not c in cur.children:
                return False
            cur = cur.children[c]
        return True


trie = Trie()
trie.insert('apple')
trie.insert('app')
trie.insert('ape')
trie.insert('beetle')

print (trie.search('apple'))
print (trie.search('beatle'))
print (trie.starts_with('app'))
print (trie.starts_with('bee'))
print (trie.find_child_words('app'))

print (trie.find_child_words('bee'))