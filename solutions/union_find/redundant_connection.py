#solves https://leetcode.com/problems/redundant-connection/
class Solution:
    def findRedundantConnection(self, G):
        N = len(G)
        p = [i for i in range(N)]
        r = [0] * N

        def f(u):
            if p[u] != u:
                p[u] = f(p[u])
            return p[u]

        def un(u, v):
            u, v = f(u), f(v)
            if r[u] > r[v]:
                p[v] = u
            else:
                p[u] = v
                if r[u] == r[v]:
                    r[v] += 1

        for u, v in G:
            u, v = u - 1, v - 1
            if f(u) == f(v):
                return [u + 1, v + 1]
            un(u, v)