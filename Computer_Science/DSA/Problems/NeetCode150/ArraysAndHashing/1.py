# 1 - Two Sum (easy)
# Topics - Array, Hashing

# You are given an array of integers nums and a int target, return the indices of the two numbers such that they add up to target

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# I don't think sorting is a solution here

# Solution 1: Brute Force
# We can double loop through the list and see if we have 2 indices that are not the same with a if check that add up to target
# Time - O(n^2)
# Space - O(1) not using any other structures

# Solution 2: HashMap
# We'd create a map of [target - nums[i]] = index
# We would loop through the original list again and check if the value at the index even exists in the map. If it does that mean we have a pair. We also check if the value of that map component is not the current index because then we'd be adding with outselves. We'd then return the current index int he loop and the value of hashmap[value]
# Time - O(n) since we just loop
# Space - O(n) since we have to make a set


def a(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        hashmap[target - nums[i]] = i
    for j in range(len(nums)):
        if hashmap[nums[j]] is not None and hashmap[nums[j]] != j:
            return [hashmap[nums[j]], j]


print(a([2, 7, 11, 15], 9))

# Given -> int array nums
# -> int target
# Return -> indices of two numbers such that they add up to target

# Brute Force -> for every val we loop through every other val and check if they add up to target and return indicies (check that i != j too) -> O(n^2)

# I don't think there is a sorting solution because you lose track of the indices maybe ; yeah i dont think theres a solution involving sorting

# The nice little trick with hashmaps and flipping the equation around -> O(n)
# target = num1 + num2
# num2 = target - num1
#
# EX -> [2,7,11,15], target = 9
#
# We want to put everything into a hashmap and then loop through it to find that num2. Perhaps we can fit all the target - num1 into the hash
# What would the key and value be?
# For now lets try:
# key = num i
# value = target - num i aka num 2
#
# [2,7,11,15], target = 9
# dic -> {7: 2, : 2, 11: -2, 15: -6}
#

# def two_sum(nums, target):
#     dic = {}
#     for i in range(len(nums)):
#         # The index of where target-nums[i] is
#         dic[target - nums[i]] = i
#     for j in range(len(nums)):
#         if dic.get(nums[j]) is not None and ...


# Attempt 3
# Given an array nums and a target find the vals that equate to target

# target - num[i] = i
# 2, 7, 11 ; target = 9
# dic = {7: 0, 2: 1, 2: 3}


def twoSum(nums, target):
    dic = {}
    for i in range(len(nums)):
        dic[target - nums[i]] = i
    for i in range(len(nums)):
        if dic.get(nums[i]) is not None and i != dic.get(nums[i]):
            return [i, dic.get(nums[i])]
