#https://www.hackerrank.com/challenges/contacts/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import collections


class TrieNode():
    def __init__(self):
        self.count=0
        self.children = collections.defaultdict(TrieNode)


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            cur.count+=1
            cur = cur.children[c]
        cur.count+=1

    def startsWith(self, prefix: str):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return 0
        return cur.count

# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    n = int(input())
    t=Trie()
    for _ in range(n):
        op, contact = input().split()
        if op=='add':
            t.insert(contact)
        else:
            print(t.startsWith(contact))