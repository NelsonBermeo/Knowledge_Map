# 594 - Longest Harmonious Subsequence (easy)

# harmonious array -> difference between max value and min value is 1

# Given nums, return length of longest harmonious subsequence

# Subsequence -> taking out some or more elements but leaving remainder ones the same

"""
Input: nums = [1,3,2,2,5,2,3,7]

Output: 5

Perhaps we can simply just look at a number x and see if x+1 is in the list and the len = count(x) + count(x+1)

So we would add all the frequencies to a map

Then have a variable max = -inf

Then we can go through every val in nums and if nums+1 is in the map then we just do hash(nums i) + hash(nums i + 1) = new max if greater than max

"""


def a(nums):
    dic = {}
    for i in range(len(nums)):
        if dic.get(nums[i]) is None:
            dic[nums[i]] = 1
        else:
            dic[nums[i]] += 1

    max_len = float("-inf")
    for i in range(len(nums)):
        len1 = dic[nums[i]]
        len2 = 0
        if dic.get(nums[i] + 1) is None:
            continue
        else:
            len2 = dic[nums[i] + 1]
        if len1 + len2 > max_len:
            max_len = len1 + len2
    if max_len == float("-inf"):
        return 0
    return max_len
