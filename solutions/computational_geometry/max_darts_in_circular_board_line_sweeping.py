#solves https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/
from math import acos, atan2

class Solution:
    def numPoints(self, points):
        best=1
        for px,py in points:
            angles=[] #all angles where a q touches p's sweeping line's circle
            for qx,qy in points:
                if (px,py)!=(qx,qy):
                    pq=((px-qx)**2+(py-qy)**2)**0.5
                    if pq<=2*r: #if p and q share a circle
                        #calculate angles relative to x-axis and the sweeping line
                        ab=atan2((qy-py),(qx-px))
                        b=acos(pq/(2.0*r))
                        angles.append((ab-b,+1)) #go in at alpha, one more q
                        angles.append((ab+b,-1)) #go out at alpha + 2 * beta, one less q
            angles.sort(key=lambda x:(x[0],-x[1])) #in comes before out to maximize count
            count=1 #need to count p
            for _, value in angles:
                best=max(best,count:=count+value) #q touches p's circle, update best?
        return best