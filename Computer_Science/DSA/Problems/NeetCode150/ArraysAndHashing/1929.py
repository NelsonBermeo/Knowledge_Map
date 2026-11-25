# 1929 - Concatenation of Array (easy)
# Topics - Array

# Given nums of length n
# We want to create an array ans of length 2n
#   Where the tail basically is just the whole array again


def a(nums):
    for i in range(len(nums)):
        nums.append(nums[i])
    return nums


print(a([1, 2, 1]))

# Well that was easy
