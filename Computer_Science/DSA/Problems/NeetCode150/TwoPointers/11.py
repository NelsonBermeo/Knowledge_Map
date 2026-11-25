# 11 - Container with Most Water (medium)

# Given:
# Int array height of length n
# This gives us n vertical lines drawn such that two endpoints are (i, 0) & (i, height(i))
# Find the two lines that together form a container that holds the most water

"""
Ex: height = [1,8,6,2,5,4,8,3,7]
What is the biggest area we can make?
"""

# def maxArea(height):
#     areaMax = float("-inf")
#     for i in range(len(height)):
#         for j in range(i + 1, len(height)):
#             #val = min(height[i], height[j]) * (j - i)
#             if (min(height[i], height[j]) * (j - i)) > areaMax:
#                 areaMax = min(height[i], height[j]) * (j - i)
#     return areaMax


def maxArea(heights):
    l = 0
    r = len(heights) - 1
    res = 0

    while l < r:
        area = min(heights[l], heights[r]) * (r - l)
        res = max(res, area)
        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1
    return res
