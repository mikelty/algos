#https://leetcode.com/problems/palindrome-pairs/

class Solution:
    def palindromePairs(self, words):
        is_palindrome=lambda s:s==s[::-1]
        m={words[i]:i for i in range(len(words))}
        res=[]
        for w,word in enumerate(words):
            for i in range(len(word)+1):
                a,b=word[:i],word[i:]
                p,q=a[::-1],b[::-1]
                if p in words and is_palindrome(b) and m[p]!=w:
                    res.append((w,m[p]))
                if q in words and is_palindrome(a) and m[q]!=w:
                    res.append((m[q],w))
        return list(set(res))

s=Solution()
w=["abcd","dcba","lls","s","sssll"]
print(s.palindromePairs(w))