#https://leetcode.com/problems/implement-trie-prefix-tree/submissions/
from collections import defaultdict

class TrieNode():
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)


class Trie:
    """
    used for quickly searching words and prefixes
    uses less space
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return True

# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)