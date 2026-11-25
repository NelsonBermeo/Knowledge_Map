# 217 - Contains Duplicate (easy)
# Topics: Array, Hashing, Sorting

# Given nums return true if any value appears at least twice

# Solution 1: Brute Force
# You can brute force with a douple loop and check if an element appears in the rest of the array
# Time - O(n^2)
# Space - O(1)

# Solution 2: Sorting
# You can sort the array with Python's built in sort function and that'd use Timsort or Powersort which has a runtime of O(nlog(n)) then you can compare every element to the one before it and you can easily find a duplicate there.
# Time - O(nlog(n))
# Space - O(n) perhaps if our sort uses a list of some sort.

# Solution 3: HashSet
# We can simply compare set(nums) to nums
# Time - O(n) because set has to iterate through all the elements
# Space - O(n) because set is created in ram

# Solution 4: HashMap
# We can loop through nums and everytime see if nums[i] is in the hashmap, each check would be O(1)
# Time - O(n) because we have to iterate through nums
# Space - O(n) becasue our hashmap is getting filled


def a(nums):
    hashmap = {}
    for i in range(len(nums)):
        if nums[i] in hashmap:
            return True
        else:
            hashmap[nums[i]] = 1
    return False


print(a([1, 2, 3, 4]))

# Attempt 2 ->

# Given an int array nums, return true if any value appears more than once in the array.

# brute force -> for every value loop through the rest of the array and check if it's equal. O(n^2)
# sorting -> sort first and then have 2 pointers and check if the values are ever the same. O(n log(n))
# hashing -> count every value with 1 for loop and if we see it again we do true. O(n)


def hashing_version(nums):
    ls = {}
    for i in range(len(nums)):
        if ls.get(nums[i]) is not None:
            return True
        else:
            ls[nums[i]] = 1
    return False
