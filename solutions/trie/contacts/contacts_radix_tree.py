#TODO: solve https://www.hackerrank.com/challenges/contacts/problem?h_r=internal-search
#TODO: modify the visited object to be is_word
#TODO:maybe add is_leaf
#!/bin/python3

import os
import sys
from collections import defaultdict

class RadixTreeNode():
    def __init__(self,count=0,keys=None):
        self.count=count
        self.children=keys if keys else defaultdict(RadixTreeNode)

class RadixTree():
    def __init__(self):
        self.root=RadixTreeNode()

    def add(self,word):
        return self.add_helper(self.root,word)

    def add_helper(self,node,word):
        node.count+=1
        for key,child in node.children.items():
            prefix, split, rest = self.match(key, word)
            if not split:
                #complete match
                return self.add_helper(child, rest)
            if prefix:
                #partial match, need to split
                new_node=RadixTreeNode(count=child.count,keys={split:child})
                node.children[prefix]=new_node
                del node.children[key]
                return self.add_helper(new_node,rest)
        node.children[word]=RadixTreeNode(count=1)

    def count_prefix(self,word):
        return self.count_prefix_helper(self.root,word)

    def count_prefix_helper(self,node,word):
        for key,child in node.children.items():
            prefix, split, rest = self.match(key, word)
            if not rest:
                return child.count
            if not split:
                return self.count_prefix_helper(child,rest)
        return 0

    def match(self, key, word):
        i=0
        for k,w in zip(key,word):
            if k!=w:
                break
            i+=1
        return key[:i],key[i:],word[i:]

