# 704 - Binary Search (easy)

# Given an array of integers nums and target write the binary serach function
#
# [-1,0,3,4,5,9,12]


def binary_search(nums, target):
    j = len(nums) - 1
    i = 0
    while i <= j:
        middle = i + ((j - i) // 2)
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            j = middle - 1
        elif nums[middle] < target:
            i = middle + 1
    return -1
