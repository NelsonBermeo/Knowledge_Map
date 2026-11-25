# 304 - Range Sum Query 2D - Immutable (medium)
# Topics:

# Given a 2d matrix called matrix
# Handle multiple queries of the following type:


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.ls = matrix

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
