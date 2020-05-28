class BIT():
    """
    binary indexed tree (Fenwick tree)
    quickly add value to element in array and calculate prefix sum
    both operations require O(logn) time
    inspired by https://en.wikipedia.org/wiki/Fenwick_tree
    """

    def __init__(self, length=0):
        """
        note this implementation uses one-based indexing,
        but all functions uses 0-based indexing as arguments.
        :param length: length of the array
        """
        self.A = [0] * (length + 1)

    def LSB(self, i):
        """
        get least significant bit
        :return: sum of the first i elements, including the i-th element.
        """
        return i & -i

    def sum(self, i):
        """
        :param i: i-th element, 0 based indexing.
        :return: sum of the first i elements, including the i-th element.
        """
        res,i = 0,i+1
        while i > 0:
            res += self.A[i]
            i -= self.LSB(i)
        return res

    def add(self, i, a):
        """
        add a to the i-th element
        :param i: i-th element, 0-based index.
        :param a: amount added
        """
        i+=1
        while i < len(self.A):
            self.A[i] += a
            i += self.LSB(i)

