# 27 - Remove Element (easy)
# Topics: Array, Two Pointers

# Given an integer array nums and an integer val remove all occurance of val in place

# Solution 1 - Two Pointer
# We can have a pointer k for the valid part of the list and we loop through with i to skip val
# Time - O(n)
# Space - O(1)


def a(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    for i in range(k + 1, len(nums)):
        nums[i] = "_"
    return nums


# Even though our time is great as is, we can optimize this further. When there are few val's in the list we do many unessesary copies. Instead we can swap unwanted elements with elements from the end of the array since we don't care about order:

# i = 0
# n = len(nums)
# while i < n:
#     if nums[i] == val:
#         n -= 1
#         nums[i] = nums[n]
#     else:
#         i += 1
# return n


print(a([0, 1, 2, 2, 3, 0, 4, 2], 2))
