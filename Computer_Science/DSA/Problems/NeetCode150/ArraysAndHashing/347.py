# 347 - Top K Frequent Elements (medium)
# Topics:

# Given an int array nums, and an integer k
#  return the k most frequent elements

# space complexity O(n + m)
# time complexity O(n log(n))


def a(nums, k):
    m = {}
    for val in nums:
        if m.get(val) is None:
            m[val] = 1
        else:
            m[val] = m[val] + 1
    s = sorted(m.items(), key=lambda x: x[1], reverse=True)
    r_ls = [0] * k
    j = 0
    for key in s[:k]:
        r_ls[j] = key[0]
        j += 1
    return s


# print(a([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2))

#


# Attempt 2 ->

# Given -> int array nums & int k
# Return -> the k most frequent elements

"""
Ex: 
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]
"""

# We can go ahead and count the values using a hash
# then we can sort the hash by count
# then we can return the slice k


def top_k(nums, k):
    hashmap = {}
    for i in range(len(nums)):
        if hashmap.get(nums[i]) is None:
            hashmap[nums[i]] = 1
        else:
            hashmap[nums[i]] += 1
    # now we have the counts for everything
    # 1:4, 2:4, 3:2
    hashmap_sorted = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
    return hashmap_sorted[:k]


print(top_k([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2))
