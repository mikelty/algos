#solves https://leetcode.com/problems/longest-chunked-palindrome-decomposition/
class Solution:
    def longestDecomposition(self, text: str) -> int:
        count=0
        h1, h2=0, 0
        base1, base2 = 26, 1
        i, j = 0, len(text) - 1
        while i<=j:
            h1=h1*base1 + ord(text[i]) - ord('a') + 1
            h2=h2 + (ord(text[j]) - ord('a') + 1 ) *base2
            base2 *= base1
            if h1==h2:
                count = count + 1 if i==j else count + 2
                h1, h2 = 0, 0
                base2=1
            i, j=i + 1, j - 1
        return count + 1 if h1 else count