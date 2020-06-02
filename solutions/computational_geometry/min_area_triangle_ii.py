#solves https://leetcode.com/problems/minimum-area-rectangle-ii/
from itertools import combinations
from collections import defaultdict

class Solution:
    def minAreaFreeRect(self, points):
        def perpendicular(px,py,qx,qy):
            return px*qx+py*qy==0
        def area(px,py,qx,qy):
            return abs((px-qx)*(py-qy))
        ans=1e30
        point_sum=defaultdict(list)
        for (px,py),(qx,qy) in combinations(points,2):
            pq=( (px+qx), (py+qy) )
            point_sum[pq].append( ( (px,py),(qx,qy) ) )
        for pairs in point_sum.values():
            for ( (px,py), (qx,qy) ), ( (rx,ry), (sx,sy) ) \
            in combinations(pairs,2):
                prx,pry=px-rx,py-ry
                psx,psy=px-sx,py-sy
                if prx*psx + pry*psy == 0:
                    ans=min(ans,abs(prx*psy - pry*psx))
        return 0 if ans==1e30 else ans
