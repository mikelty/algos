#solves https://leetcode.com/problems/the-skyline-problem/
#from derek3 https://leetcode.com/problems/the-skyline-problem/discuss/61198/My-O(nlogn)-solution-using-Binary-Indexed-Tree(BIT)Fenwick-Tree
class Solution:
    def getSkyline(self, buildings):
        def update(right_end, height):
            """
            when we hit a building's left wall during the scan,
            we require all the points overlapping the building
            to have at least its height. this is done by a
            modified version of fenwick tree, in which we only
            take the max of the indices to the left of the
            building's right end.
            :param right_end: index of right end of building
            :param height: building's height
            :return: None
            """
            while right_end>0:
                bit[right_end]=max(bit[right_end],height)
                right_end-=right_end & -right_end

        def query(loc):
            """
            queries every building that loc is in and return their
            maximal height.
            :param loc: x coordinate of the queried location
            :return: largest height of the building which loc is in
            """
            height=0
            while loc<len(bit):
                height=max(height,bit[loc])
                loc+=loc & -loc

        locations = []
        for i, (start, end, height) in enumerate(buildings):

