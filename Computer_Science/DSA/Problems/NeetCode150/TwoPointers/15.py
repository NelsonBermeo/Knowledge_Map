# 15 - 3Sum (medium)

# Given an integer array nums return all the triplets
# Such that they are not equal idx
# and their values add up to 0

# Brute force seems to be a 3 loop nested approach but that would be O(n^3) complexity

"""
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Sorted = [-4, -1, -1, 0, 1, 2]

i + j + k = 0 -> i + j = -k
"""

# def threeSum(nums):
#     dic = {}
#     for i in range(len(nums)):
#         dic[]
