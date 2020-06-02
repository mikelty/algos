#solves https://leetcode.com/problems/distinct-echo-substrings/
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        base,mod=29,10**9+7
        h,p=[0],[1]
        for c in text:
            h.append( ( h[-1]*base + ord(c) ) %mod )
            p.append( ( p[-1]*base ) %mod )
        ans=set()
        for i in range(len(text)):
            for l in range(2,len(text)+1-i,2):
                mid=i+l//2
                get_hash=lambda lo,hi : ( h[hi] - h[lo]*p[hi - lo]%mod + mod ) %mod
                if get_hash(i,mid)==get_hash(mid,i+l):
                    ans.add(get_hash(i,mid))
        return len(ans)