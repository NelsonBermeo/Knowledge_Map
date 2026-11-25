# 169 - Majority Element (easy)
# Topics - Array, HashTable, Divide & Conquer, Sorting, Counting, Boyer-Moore Majority Vote Algorithm

# Given an array nums of size n return the majority element. A majority element is the element that appears more than floor(n / 2) times.

# Ex:
# [2,2,1,1,1,2,2] ; majority = 2

# First
# Just get the length
# Find the majority number
# Loop through nums and make map with count of each element
# Then go through map and return the one with  > majority
# Time - O(n) - we only loop
# Space - O(n) - dictionary
import math


def a(nums):
    m = {}
    maj = math.floor(len(nums) / 2)
    for i in range(len(nums)):
        if m.get(nums[i]) is None:
            m[nums[i]] = 1
        else:
            m[nums[i]] += 1

    for key, vals in m.items():
        if vals > maj:
            return key


print(a([2, 2, 1, 1, 1, 2, 2]))
