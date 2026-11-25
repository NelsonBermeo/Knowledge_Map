# 219 - Contains Duplicate 2 (easy)

# Given an integer array nums and an integer k, return true if there are two distint indices such that nums[i] = nums[j] AND abs(i-j) <= k

# The k part of this problem is reffering to the space between the indicies has to be k or less than k

"""
Ex:
Input: nums = [1,2,3,1], k = 3
i = 0; j = 3
Output: true

Input: nums = [1,2,9,3,5,3,10,2] k = 2
i = 3; j = 5
Output: true


"""


def a(nums, k):
    """
    Maybe we can try having a window of size k+1 and if there is a duplicate within it we can return true ;
    So we can loop through it with our window, but how will we find if there is a duplicate? Maybe we can use a hashmap there?
    """
    window = set()  # This would represent our window
    L = 0  # this is the left index for our window

    for R in range(len(nums)):  # The R is our right index for the window
        if R - L > k:  # If our window gets too big
            window.remove(nums[L])  # we remove the left index and add 1 to it
            L += 1
        if nums[R] in window:
            return True  # If we the value in our window then we have a duplicate
        window.add(nums[R])
    return False
