class Solution:
    """
    solves https://leetcode.com/problems/the-skyline-problem/
    from derek3 https://leetcode.com/problems/the-skyline-problem/discuss/61198/My-O(nlogn)-solution-using-Binary-Indexed-Tree(BIT)Fenwick-Tree
    another way to use BIT
    """
    def getSkyline(self, buildings):
        def update(p,h):
            while p>0:
                bit[p]=max(bit[p],h)
                p-=p&-p

        def query(p):
            ans=0
            while p<=len(bit):
                ans=max(ans,bit[p])
                p+=p&-p
            return ans

        ret, points, end = [], [], {}
        for i, b in enumerate(buildings):
            points += ((b[0], -1, -b[2]), (b[1], 1, -b[2]))
            end[points[-2]]=points[-1]
        points.sort()
        bit=[0]*(len(points)+1)
        idx={points[i]:i for i in range(len(points))}

        for i,p in enumerate(points):
            if p[1]==-1:
                e=end[p]
                update(idx[e],-p[2])
            h=query(i+1)
            if not ret or ret[-1][1]!=h:
                if ret and ret[-1][0]==p[0]:
                    ret[-1][1]=h
                else:
                    ret.append([p[0],h])
        return ret
