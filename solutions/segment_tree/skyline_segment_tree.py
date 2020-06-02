#solves https://leetcode.com/problems/the-skyline-problem/
#from derek3 https://leetcode.com/problems/the-skyline-problem/discuss/61198/My-O(nlogn)-solution-using-Binary-Indexed-Tree(BIT)Fenwick-Tree
class SegmentTreeNode():
    def __init__(self,start,end,height):
        """
        initialize segment tree node for skyline problem
        :param start: start index of this node's interval
        :param end: end index of this node's interval
        :param height: minimal height of this node's interval
        """
        self.start=start
        self.end=end
        self.height=height

    def add(self,start,end,height):
        """
        adds a o
        :param start:
        :param end:
        :param height:
        :return:
        """
class Solution:
    def getSkyline(self, buildings):
