class SegmentTree():
    pass
class Solution:
    #perhaps add a building from -inf to inf of height 0
    def getSkyline(self, buildings):
        buildings.append([-2**30,2**30,0])
        intervals=[tuple(building[:1]) for building in buildings]
        queries = [x for interval in intervals for x in interval]
        heights={intervals[i]:buildings[i][-1] for i in range(len(buildings))}
        st=SegmentTree(intervals)
        result=[]
        for x in queries:
            segments=st.query(x)
            #discard segments that have x as its right end
            segments=[segment for segment in segments if segment[1]!=x]
            result.append([x,max(heights[tuple(segment)] for segment in segments)])
        return result[1:]