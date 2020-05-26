import collections

class TrieNode():
    def __init__(self):
        self.is_word=False
        self.children=collections.defaultdict(TrieNode)

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur=self.root
        for c in word:
            cur=cur.children[c]
        cur.is_word=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        print(word)
        def search_helper(node,word):
            if not word:
                return True
            for i,c in enumerate(word):
                if c=='.':
#                    return any(search_helper(child,word[i+1:]) for child in node.children)
                    for child in node.children.values():
                        if search_helper(child,word[i+1:]):
                            return True
                elif c in node.children:
                    node=node.children[c]
                else:
                    return False
            return node.is_word
        return search_helper(self.root,word)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
#obj.search("pad") # false
#obj.search("bad") # true
obj.search(".ad") # true
obj.search("b..") # true