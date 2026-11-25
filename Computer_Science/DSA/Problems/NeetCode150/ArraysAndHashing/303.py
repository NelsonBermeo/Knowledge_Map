# 303 - Range Sum Query - Immutable (easy)
# Topics: Prefix Sum

# Given an integere array nums
# Handle multiple queries of:
# calculate the sum of the elements of nums between left and right inclusive


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ls = nums
        self.p_sum = []

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
