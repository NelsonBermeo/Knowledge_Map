# 49 - Group Anagrams (medium)
# Topics - Array, Hashing, String, Sorting

# Given an array of strings strs, group the anagrams together

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Solution 1 - Sorting
# We can create a hashmap where each key is the sorted version of a string and the value is a list of strings
# We iterate through each string in the input list and append the original string to the list corresponding to the key
# Then we add every value into a list and return
# Complexity - O(m * nlog(n)) because we have to sort every string
# Space ...

# Solution 2 - Hash Table with 26 len list
# Instead of sorting each string, we can represent every string by the frequency of its characters. Since the problem uses lowercase English a fixed array of 26 can capture how many times each char appears. Two string are anagrams if their frequency arrays match


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord("a")] += 1
#             res[tuple(count)].append(s)
#         return list(res.values())


# Attempt 2

# Given -> array of strs
# Return -> group the anagrams together
"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

# First thought, can we use the solution for 1 anagram here?
# We remember that its simply just creating hashmaps; first lets look at the sorted solution.

# So if we sort every word we'd have a couple words that look the same.
# count[sortedword] = [indexes]
# And then for every value I can append a new list with those indexes
# That'd be okay -> O(m * n log(n)) -> m is number of strings and n is length of longest string
# Even attempting to make a hashmap for every word would be a memory tragedy

# Method 2 ->
# really chill, just have a default dict (all values start at 0 without an error trying to access) and for every word
# we would just make a alpahabet list and add 1 to every char that appears
# then we use this list as the key for the dict and the value is the word
# so when another word (anagram) has the same key and its added we have a dict where all the values are the groups of the anagrams
# then we just return list of values
# runtime -> O(n * k) since we have to run at worst on the longestaqA string len(s) = k
# space -> O(m * 26) where m is the number of words in list because those are counts

from collections import defaultdict


def group_anagrams(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    return list(res.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
