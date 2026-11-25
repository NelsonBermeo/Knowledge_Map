# 75 - Sort Colors (medium)
# Topics:

# Given an array nums with n objects colored red, white or blue
# Sort them in place so that objects of the same color are adjacent with the order red, white, blue
# We will use the ints 0,1,2 to represent the respective colors
# Do not use the sort function

# Ex:
# nums = [2,0,2,1,1,0]
# [0,0,1,1,2,2]

# [1,2,1,2]

# Space complexity - O(1)
# Time complexity - O(n) log(n)


def a(nums):
    # First, let's find the proper indices for our endings of 0 and 1
    zero_count = 0
    one_count = 0
    for val in nums:
        if val == 0:
            zero_count += 1
        if val == 1:
            one_count += 1
    # [p,p,p,p,p,p]
    #    ^   ^
    #   z_c  o_c

    i = 0
    for id in range(len(nums)):
        if nums[id] == 0:
            temp = nums[i]
            nums[i] = nums[id]
            nums[id] = temp
            i += 1
    j = zero_count
    for id in range(zero_count, len(nums)):
        if nums[id] == 1:
            temp = nums[j]
            nums[j] = nums[id]
            nums[id] = temp
            j += 1
    return nums


print(a([1, 2, 1, 2]))
